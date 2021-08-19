import math
N = 10**5 + 10
u = [-1] * N
divi = [[] for i in range(N)]
pd = [[] for i in range(N)]
mark = [0] * N


def precalc():
    for i in range(1, N):
        for j in range(i, N, i):
            divi[j].append(i)
        if i == 1:
            u[i] = 1
        elif (i // divi[i][1]) % divi[i][1] == 0:
            u[i] = 0
        else:
            u[i] = -u[i // divi[i][1]]


has = [False] * N
cnt = [0] * N


def has_coprime(n):
    ret = 0
    for d in divi[n]:
        ret += u[d] * cnt[d]
    return ret


def update(n, val):
    for d in divi[n]:
        cnt[d] += val


def solve(n):
    li = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if has[li[i]]:
            ans = max(ans, li[i])
        has[li[i]] = True

    for g in range(1, N):
        st = []
        for num in reversed(list(range(1, N // g + 1))):
            if num * g > N - 1 or not has[num * g]:
                continue
            how_many = has_coprime(num)

            while how_many > 0:
                # print(how_many)
                now = st.pop()
                if math.gcd(now, num) == 1:
                    ans = max(ans, num * now * g)
                    how_many -= 1
                update(now, -1)
            st.append(num)
            update(num, 1)
        while st:
            update(st.pop(), -1)

    print(ans)


precalc()

while True:
    try:
        n = int(input())
        solve(n)
    except EOFError:
        break

mod = 10 ** 9 + 7


def solve():
    (a, b) = map(int, input().split())
    s = input()
    v = []
    tmp = 0
    ok = False
    for i in range(len(s)):
        if s[i] == '1':
            if tmp > 0:
                v.append(tmp)
            tmp = 0
            ok = True
        elif ok:
            tmp += 1
    v.sort()
    ans = a * (len(v) + 1)
    if not ok:
        ans = 0
    for i in range(len(v)):
        if ans >= ans - a + b * v[i]:
            ans = ans - a + b * v[i]
        else:
            break
    print(ans)


t = 1
t = int(input())
while t > 0:
    solve()
    t -= 1

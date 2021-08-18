f_memo = {0: 1, 1: 1}


def f(x):
    nonlocal f_memo
    if x in f_memo:
        return f_memo[x]
    else:
        res = x * f(x - 1)
        f_memo[x] = res
        return res


comb_memo = {}


def comb(n, r):
    nonlocal comb_memo
    if (n, r) in comb_memo:
        return comb_memo[(n, r)]
    else:
        a = f(n)
        b = f(n - r)
        c = f(r)
        res = a // b // c
        comb_memo[(n, r)] = res
        return res


N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

mu = sum(v[:A]) / A
R = A - 1
for i in range(A, N):
    if v[i] == mu:
        R = i
    else:
        break

R += 1
ans = 0
if R > A:
    for i in range(A, B + 1):
        if i > R:
            break
        ans += comb(R, i)
else:
    min_v = v[A - 1]
    n = v.count(min_v)
    need = v[:A].count(min_v)
    ans += comb(n, need)

print(mu)
print(ans)

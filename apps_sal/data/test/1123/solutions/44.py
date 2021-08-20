(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
ans = [0] * (k + 1)
anss = 0
for i in reversed(range(1, k + 1)):
    ans[i] = pow(k // i, n, mod)
    for j in range(2, k // i + 1):
        ans[i] -= ans[i * j]
    anss += i * ans[i]
    anss %= mod
print(anss)

N, M = map(int, input().split())
div = []
for i in range(2, int(M**(1 / 2)) + 2):
    cur = 0
    while M % i == 0:
        M = M // i
        cur += 1
    if cur >= 1:
        div.append(cur)
if M > 1:
    div.append(1)
div.sort()
mod = 10**9 + 7
frac = [1] * (N + 50)
num = len(frac)
for i in range(len(frac) - 1):
    frac[i + 1] = frac[i] * (i + 1) % mod
finv = [1] * (N + 50)
finv[-1] = pow(frac[-1], mod - 2, mod)
for i in range(1, num):
    finv[num - 1 - i] = finv[num - i] * (num - i) % mod
ans = 1
for i in div:
    ans = ans * frac[N + i - 1] * finv[N - 1] * finv[i] % mod
print(ans)

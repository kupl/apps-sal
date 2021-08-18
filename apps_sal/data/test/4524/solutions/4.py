TOT = 2 * 10**5
mod = 998244353
aux = [0] * (TOT + 1)
aux[0] = 1
for i in range(1, len(aux)):
    aux[i] = (2 * aux[i - 1]) % mod

n, m = [int(x) for x in input().split()]

a = input()[::-1]
ar = [0] * (TOT + 1)
for i in range(n):
    if i:
        ar[i] = ar[i - 1]
    if a[i] == '1':
        ar[i] = (ar[i] + aux[i]) % mod

b = input()[::-1]
ans = 0
for i in range(m):
    if b[i] == '1':
        if i >= n:
            ans = (ans + ar[n - 1]) % mod
        else:
            ans = (ans + ar[i]) % mod


print(ans)

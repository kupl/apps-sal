from copy import deepcopy
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mod = 10 ** 9 + 7
ans = 1
i, j = 0, n - 1
k2 = deepcopy(k)
while k2 > 1:
    if a[i] * a[i + 1] > a[j] * a[j - 1]:
        ans *= a[i] * a[i + 1]
        ans %= mod
        i += 2
        k2 -= 2
    else:
        ans *= a[j]
        j -= 1
        ans %= mod
        k2 -= 1
if k2 == 1:
    ans *= a[j]
    ans %= mod
if a[-1] < 0 and k % 2:
    ans = 1
    for i in range(n - k, n):
        ans *= a[i]
        ans %= mod
print(ans)

import sys
n, k = list(map(int, input().split()))
if k == 0:
    print((n * n))
    return
ans = n * n
for b in range(1, n + 1):
    if b <= k:
        ans -= n
        continue
    ans -= (n + 1) // b * k - 1
    ans -= min((n + 1) % b, k)
print(ans)

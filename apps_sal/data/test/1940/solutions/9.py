import sys
n, k = list(map(int, input().split()))
w = list(map(int, input().split()))
rem = 0
ans = 0
for i in range(n):

    if w[i] % k != 0:
        rem += 1
    ans += w[i] // k
res = 0
res += ans // 2
if ans % 2 != 0:
    rem += 1
res += rem // 2
if rem % 2 != 0:
    res += 1
print(res)

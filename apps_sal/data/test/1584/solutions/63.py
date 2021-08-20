from bisect import *
n = int(input())
L = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        k = bisect_right(L, L[i] + L[j] - 1)
        ans += k - j - 1
print(ans)

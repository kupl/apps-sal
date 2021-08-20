from bisect import bisect_left
n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += bisect_left(L, L[i] + L[j]) - j - 1
print(ans)

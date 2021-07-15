from bisect import bisect_left

n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        k = l[i] + l[j]
        pos = bisect_left(l, k)
        ans += max(0, pos - j - 1)
print(ans)

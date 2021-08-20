import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 1, 1, -1):
    for j in range(i - 1, 0, -1):
        t = bisect.bisect_right(a, a[i] - a[j])
        if j - t > 0:
            ans += j - t
print(ans)

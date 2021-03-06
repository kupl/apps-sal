import bisect
n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        x = bisect.bisect_left(l, l[i] + l[j]) - j - 1
        ans += max(0, x)
print(ans)

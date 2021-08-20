import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        (l1, l2) = (l[i], l[j])
        ans += max(bisect.bisect_left(l, l1 + l2) - j - 1, 0)
print(ans)

from bisect import bisect_left
n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = bisect_left(l, l[i] + l[j])
        ans += a - 1 - j
print(ans)

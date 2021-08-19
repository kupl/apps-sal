import bisect
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
cd.sort(key=lambda x: x[0])
ans = 0
i = 0
red_x = []
for (c, d) in cd:
    while i < n and ab[i][0] < c:
        bisect.insort_right(red_x, ab[i][1])
        i += 1
    if red_x and red_x[0] < d:
        idx = bisect.bisect_right(red_x, d) - 1
        ans += 1
        red_x.pop(idx)
print(ans)

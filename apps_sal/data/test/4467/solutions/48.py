import bisect
N = int(input())
R = [tuple(map(int, input().split())) for i in range(N)]
B = [tuple(map(int, input().split())) for i in range(N)]

R.sort()
B.sort()
i = 0
ans = 0
red_y = []
for b_x, b_y in B:
    while i < N and R[i][0] < b_x:
        bisect.insort_right(red_y, R[i][1])
        i += 1
    if red_y and red_y[0] < b_y:
        idx = bisect.bisect_right(red_y, b_y) - 1
        ans += 1
        red_y.pop(idx)
print(ans)

n = int(input())
xyh = []
for i in range(n):
    x, y, h = map(int, input().split())
    xyh.append([h, x, y])
xyh.sort(reverse=True)
ans = 0

for cx in range(101):
    for cy in range(101):
        for N in range(n):
            if abs(xyh[0][1] - cx) + abs(xyh[0][2] - cy) + xyh[0][0] > 0:
                H = abs(xyh[0][1] - cx) + abs(xyh[0][2] - cy) + xyh[0][0]
            else:
                break
            if xyh[N][0] != max(H - abs(xyh[N][1] - cx) - abs(xyh[N][2] - cy), 0):
                break
            if N == n - 1:
                ans = [cx, cy, H]
print(*ans)

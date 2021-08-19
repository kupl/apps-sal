n = int(input())
heights = list(map(int, input().split()))
cnt = 1
max = heights[0]
for p in range(n):
    if p == 0:
        continue
    elif max <= heights[p]:
        max = heights[p]
        cnt += 1
print(cnt)

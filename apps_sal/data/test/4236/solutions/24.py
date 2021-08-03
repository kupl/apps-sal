n, m = list(map(int, input().split()))
used_points = [False] * (m + 1)
for ind in range(n):
    l, r = list(map(int, input().split()))
    for point in range(l, r + 1):
        used_points[point] = True

count_not_used = 0
res = ''
for point in range(1, m + 1):
    if not used_points[point]:
        count_not_used += 1
        res += str(point) + ' '

print(count_not_used)
print(res)

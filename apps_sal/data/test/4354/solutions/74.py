n, m = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(m)]
ans = []
for i in range(n):
    min_diff = 20 ** 8 + 1
    near_point = 0
    for j in range(m):
        diff = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
        if diff < min_diff:
            min_diff = diff
            near_point = j + 1
    ans.append(near_point)
print("\n".join(map(str, ans)))

(n, m) = map(int, input().split())
student = [None] * n
for i in range(n):
    student[i] = tuple(map(int, input().split()))
point = [None] * m
for i in range(m):
    point[i] = tuple(map(int, input().split()))
for i in range(n):
    dist = pow(10, 9)
    ans = 0
    (x, y) = student[i]
    for j in range(m):
        sub = abs(point[j][0] - x) + abs(point[j][1] - y)
        if dist > sub:
            dist = sub
            ans = j + 1
    print(ans)

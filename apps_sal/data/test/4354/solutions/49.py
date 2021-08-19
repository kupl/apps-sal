(N, M) = map(int, input().split())
students = []
points = []
for _ in range(N):
    students.append(list(map(int, input().split())))
for _ in range(M):
    points.append(list(map(int, input().split())))
for i in range(N):
    MIN = 10 ** 10
    index = -1
    for j in range(M):
        if MIN > abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1]):
            MIN = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
            index = j
    print(index + 1)

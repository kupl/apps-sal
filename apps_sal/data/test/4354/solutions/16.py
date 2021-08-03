n, m = list(map(int, input().split()))

students = []
for _ in range(n):
    students.append(list(map(int, input().split())))

checks = []
for _ in range(m):
    checks.append(list(map(int, input().split())))

for student in students:
    index = 1
    min = 10**8 * 4
    for i, check in enumerate(checks, 1):
        tmp = abs(student[0] - check[0]) + abs(student[1] - check[1])
        if min > tmp:
            min = tmp
            index = i
    print(index)

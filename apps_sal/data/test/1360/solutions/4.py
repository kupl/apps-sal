n=int(input())
exams = []
for i in range(n):
    a = input().split(' ')
    exams.append([int(a[0]), int(a[1])])
exams.sort()
days = 0
for item in exams:
    if item[1] < days:
        days = item[0]
    else:
        days=item[1]
print(days)


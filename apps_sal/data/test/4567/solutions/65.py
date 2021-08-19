g = int(input())
grades = []
for i in range(g):
    grade = int(input())
    grades.append(grade)
total = sum(grades)
grades.sort()
grades = [0] + grades
count = 0
for grade in grades:
    if (total - grade) % 10 != 0:
        print(total - grade)
        break
    else:
        count += 1
if count == len(grades):
    print(0)

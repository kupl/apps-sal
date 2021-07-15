n = int(input())

grades = [int(x) * 2 for x in input().split()]

res = sum(grades)
target = 9 * len(grades)

grades.sort()

for i, grade in enumerate(grades):
    if res >= target:
        print(i)
        break
    else:
        res += 10 - grade
else:
    print(len(grades))


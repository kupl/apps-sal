n = int(input())
grades = list(map(int, input().split()))
grades.sort()
cur = sum(grades) / len(grades)
i = 0
while cur < 4.5:
	grades[i] = 5
	cur = sum(grades) / len(grades)
	i += 1
print(i)


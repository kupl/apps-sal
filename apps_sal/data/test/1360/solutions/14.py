#!/usr/bin/env python3

n = int(input())
exams = []
for _ in range(n):
	day = list(map(int, input().split()))
	exams.append(day)

exams.sort()
best = -1

for x in range(len(exams)):
	if best <= exams[x][1]:
		best = exams[x][1]
	else:
		best = exams[x][0]

print(best)

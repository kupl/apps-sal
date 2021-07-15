#!/usr/bin/env python3

[n, B] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))

c = [0, 0]
cutcost = []
for i in range(n - 1):
	c[ais[i] % 2] += 1
	if c[0] == c[1]:
		cutcost.append(abs(ais[i] - ais[i + 1]))

cutcost.sort()
cnt = 0
for cost in cutcost:
	if cost <= B:
		cnt += 1
		B -= cost

print (cnt)


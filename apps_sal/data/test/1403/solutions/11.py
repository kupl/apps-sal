#!/usr/bin/env python3

[n, K] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))

ais.sort()
res = 0
cnt = 1
for i in range(n - 1):
	if ais[i + 1] == ais[i]:
		cnt += 1
	else:
		if ais[i + 1] > ais[i] + K:
			res += cnt
		cnt = 1

res += cnt
print (res)


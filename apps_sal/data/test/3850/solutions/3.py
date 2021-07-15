#!/usr/bin/env python3
# http://codeforces.com/contest/830/problem/A
import sys
from operator import itemgetter

read = lambda: list(map(int, input().split()))
n, k, p = read() # n people, k keys, office location 
people, keys = sorted(read()), sorted(read())

res = []
for i in range(k - n + 1):
	inner_res = []
	for j in range(n):
		inner_res.append(abs(keys[i + j] - people[j]) + abs(keys[i + j] - p))
	res.append(max(inner_res))

print(min(res))


import sys
from collections import deque

n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split(' ')))
c = list(map(int, sys.stdin.readline().strip().split(' ')))

lower = [float('inf') for i in range(n)]
upper = [float('inf') for i in range(n)]
for i in range(n):
	for j in range(i):
		if s[i] > s[j]:
			lower[i] = min(lower[i], c[j])
for i in range(n-1,-1,-1):
	for j in range(i+1,n):
		if s[j] > s[i]:
			upper[i] = min(upper[i], c[j])
ans = float('inf')
for i in range(n):
	ans = min(ans, lower[i] + c[i] + upper[i])
print([-1,ans][ans!=float('inf')])

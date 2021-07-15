import sys

n = int(input())
m = float(input())
a = list(map(float,input().split()))
b = list(map(float,input().split()))

for i in a:
	if i <= 1.0:
		print(str(-1))
		return
for i in b:
	if i <= 1.0:
		print(str(-1))
		return

s = m
s += s/(b[0] - 1.0)

for i in range(n-1,0,-1):
	s += s/(a[i] - 1.0)
	s += s/(b[i] - 1.0)

s += s/(a[0] - 1.0)
print("{0:.10f}".format(s - m))

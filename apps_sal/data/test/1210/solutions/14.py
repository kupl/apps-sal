# C problem
import sys

buffer=input().split(' ')
[n, p] = [ int(buffer[i]) for i in range(len(buffer)) ]

shark = []
for i in range(n):
	buffer=input().split(' ')
	[a, b] = [ int(buffer[i]) for i in range(len(buffer)) ]
	shark.append([ int(b/p)-int((a-1)/p) , int(b-a+1) ])

result = 0.0
for i in range(n):
	[a, b] = shark[i]
	[c, d] = shark[(i+1)%n]
	temp = (float(a*d + b*c - a*c))*2000/(b*d)
	result += temp
print(result)

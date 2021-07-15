n,m = [int(i) for i in input().split()]
time = 0
import sys
while n > 0:
	if n < m:
		print(time+n)
		return
	n -= m-1
	time += m

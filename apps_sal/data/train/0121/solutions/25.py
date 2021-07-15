import sys
t = int(input())
for _ in range(t):
	n=int(input())
	l = list(map(int,sys.stdin.readline().split()))
	l.sort()
	print(l[n]-l[n-1])


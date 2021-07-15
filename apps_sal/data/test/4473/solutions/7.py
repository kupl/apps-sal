t = int(input())

for i in range(t):
	a,b,k = map(int,input().split())
	bc = k//2
	ac = k - bc
	print(a*ac-b*bc)

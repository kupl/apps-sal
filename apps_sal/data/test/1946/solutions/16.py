import sys
#sys.stdin = open("2.in") # COMMENT THIS BEFORE SUBMIT
input = sys.stdin.readline

N = int(input())
A = set()
X = {}
for i in range(N):
	a,x = map(int,input().split())
	A.add(a)
	X[a] = x
M = int(input())
B = set()
Y = {}
for i in range(M):
	b,y = map(int,input().split())
	B.add(b)
	Y[b] = y

s1 = sum([X[x] for x in A - B])
s2 = sum([Y[y] for y in B - A])
s3 = sum([max(X[x],Y[x]) for x in A & B])
print(s1+s2+s3)

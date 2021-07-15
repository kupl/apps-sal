import sys
import math
input = sys.stdin.readline

a,b,c,d=map(int,input().split())

l=[a,b,c]
l.sort()

d1=l[1]-l[0]
d2=l[2]-l[1]

count=0
if d1<d:
	count+=d-d1
if d2<d:
	count+=d-d2

print(count)

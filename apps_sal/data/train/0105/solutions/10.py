import sys
import math
def II():
	return int(sys.stdin.readline())
 
def LI():
	return list(map(int, sys.stdin.readline().split()))
 
def MI():
	return list(map(int, sys.stdin.readline().split()))
 
def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
    n,k = MI()
    a = LI()
    a.sort()
    count = 0
    for i in range(1,n):
        b = max(k-a[i],0)
        count+=b//a[0]
    print(count)


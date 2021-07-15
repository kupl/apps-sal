
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline
mii=lambda:list(map(int,input().split()))

a,b,c=mii()
b-=1
c-=2
print(min(a,b,c)*3+3)


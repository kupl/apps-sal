
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline
mii=lambda:list(map(int,input().split()))

a,b,c=mii()
d=min(a,b)
a-=d
b-=d
c+=d

print(c*2+min(1,max(a,b)))



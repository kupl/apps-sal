
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

stuff=list(map(int,input().split()))

a=min(stuff)
b=max(stuff)

ans=0

for i in stuff:
    if a<i<b:ans+=1
print(ans)


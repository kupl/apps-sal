
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

ans=10**9

for i in range(1,2000):
    if i*i>=n:
        ans=i*4
        break
    if i*(i+1)>=n:
        ans=i*4+2
        break

print(ans)

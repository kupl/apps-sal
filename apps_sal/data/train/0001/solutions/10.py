
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

for _ in range(int(input())):
    n,m,k=list(map(int,input().split()))
    n=abs(n)
    m=abs(m)
    if max(n,m)>k:
        print("-1")
    else:
        # you can't 0 0 1 me :D
        bad1=((n+k)%2==1)
        bad2=((m+k)%2==1)
        print(k-bad1-bad2)


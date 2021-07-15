import sys
n,t=list(map(int,input().split()))
l=list(map(int,input().split()))
sum=0

for i in range(n):
    sum+=86400-l[i]
    if sum>=t:
        print(i+1)
        return



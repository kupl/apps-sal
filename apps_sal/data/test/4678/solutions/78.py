n=int(input())
lst=list(map(int,input().split()))

now=lst[0]
sm=0

for i in range(1,n):
    if lst[i]>=now :
        now=lst[i]
        continue
    sm+=now-lst[i]

print(sm)

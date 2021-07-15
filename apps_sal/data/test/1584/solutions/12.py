import bisect
n=int(input())
lis=list(map(int, input().split())) 
lis.sort()
out=0
for i in range(n):
    for j in range(1+i,n):
        out+=bisect.bisect_left(lis,lis[i]+lis[j])-j-1
print(out)

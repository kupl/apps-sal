import bisect
n=int(input())
arr=list(map(int,input().strip().split(' ')))
mx=0
i=n-2
cnt=1
while(i>=0):
    if(2*arr[i]>=arr[i+1]):
        cnt+=1
    else:
        mx=max(cnt,mx)
        cnt=1
    i-=1
print(max(cnt,mx))


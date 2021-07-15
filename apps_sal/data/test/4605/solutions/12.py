N,A,B = list(map(int,input().split()))

ans=0

for i in range(1,N+1):
    sum_all=0
    tmp=i
    while(tmp>9):
        sum_all += tmp%10
        tmp//=10
    sum_all += tmp

    if sum_all>=A and sum_all<=B:
        ans+=i
        # print(i)

print(ans)


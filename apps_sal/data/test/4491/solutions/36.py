N = int(input())
A1= list(map(int,input().split()))
A2= list(map(int,input().split()))
sum2 = sum(A2)
ans = A1[0]+sum2
value = A1[0]+sum2
for i in range(1,N):
    value = value + A1[i] - A2[i-1]
    ans = max(ans,value)
print(ans)

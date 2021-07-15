n=int(input())
a=list(map(int,input().split()))
num1=[0]*(2*(10**5)+10)
num2=[0]*(2*(10**5)+10)
for i in range(n):
    if a[i]+i+1<2*(10**5)+5:
        num1[a[i]+i+1]+=1
    if a[i]+1<i+1:
        num2[-a[i]+i+1]+=1
ans=0
for i in range(len(num1)):
    ans+=num1[i]*num2[i]
print(ans)


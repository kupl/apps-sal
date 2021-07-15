n=int(input())
ip1=list(map(int,input().split()))
ip2=list(map(int,input().split()))
ans=0
ans2=0
for i in range(n):
    ans=ans|ip1[i]
for j in range(n):
    ans2=ans2|ip2[j]
print(ans+ans2)


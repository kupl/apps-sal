p=10**5+9 
t=[[] for i in range(p)]
dp=[0]*p
for i in range(2,p):
    if not t[i]:
        t[i].append(i)
    for j in range(2*i,p,i):
        t[j].append(i)              #store the divisors 
n=int(input())
l=[int(i) for i in input().split()]
if n==1:
    print(1)
    return 
for i in l:
    #explore divisors what is dp of them 
    maxi=0 
    for j in t[i]:
        maxi=max(maxi,dp[j])
    dp[i]=maxi+1 
    for j in t[i]:
        dp[j]=maxi+1 
#print(dp[0:10])
print(max(dp))

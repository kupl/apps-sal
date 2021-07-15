N=int(input())
Wls=list(map(int,input().split()))

accum_Wls=[0]
for W in Wls:
    accum_Wls.append(accum_Wls[-1]+W)

# print(accum_Wls)

ans=10**9+13

for i in range (1,N):
    temp=abs((accum_Wls[-1]-accum_Wls[i])-accum_Wls[i])
    if temp<ans:
        ans=temp

print(ans)

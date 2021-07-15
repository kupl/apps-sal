n=int(input())
memo=[0]*110
memo[1]=1
for i in range(2,105):
    memo[i]=memo[i-1]+i
print(memo[n])

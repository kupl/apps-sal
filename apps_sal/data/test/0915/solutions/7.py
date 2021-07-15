import sys
input = sys.stdin.readline
k=int(input())
w="codeforces"
nums=[1]*10
prod=1
i=0
while prod<k:
    prod//=nums[i]
    nums[i]+=1
    prod*=nums[i]
    i+=1
    if i==10:
        i=0
sol=""
for i in range(10):
    for j in range(nums[i]):
        sol+=w[i]
print(sol)

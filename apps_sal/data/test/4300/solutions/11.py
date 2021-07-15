n = int(input())
li = list(map(int,input().split()))
su = 0
for i in range(n):
    for j in range(i+1,n):
        su += li[i]*li[j]

print(su)

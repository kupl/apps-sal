n = int(input())
pi = list(map(int,input().split()))
ab = input()

numi = [0]*n
numi2 = [0]*n
if ab[0] == "B":
    numi[0] = pi[0]
else:
    numi2[0] = pi[0]
    
for i in range(1,n):
    if ab[i] == "B":
        numi[i] = numi[i-1] + pi[i]
        numi2[i] = numi2[i-1]
    else:
        numi2[i] = numi2[i-1] + pi[i]
        numi[i] = numi[i-1]
n2 = n-1
maxi = numi[n2] 
for i in range(n):
    maxi = max(maxi,numi[n2] - numi[i] + numi2[i])
for i in range(n-2,-1,-1):
    maxi = max(maxi,numi[i] + numi2[n2] - numi2[i])
print(maxi)


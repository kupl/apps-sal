n, m = list(map(int, input().split()))
L = list(map(int, input().split()))
T = [0 for _ in range(m)]
for k in range(n):
    T[L[k]-1]+=1
r = 0
for i in range(m-1):
    for j in range(i+1,m):
        r+= T[i]*T[j]
print(r)


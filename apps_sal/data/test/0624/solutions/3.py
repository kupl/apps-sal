n,k,m = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

L.sort(reverse = True)

T = [0]

for i in range(n):
    T.append(T[-1]+L[i])
    
best = 0
for i in range(1,n+1):
    if n-i <= m:
        best = max(best,(T[i]+min(m-n+i,k*i))/i)

print(best)

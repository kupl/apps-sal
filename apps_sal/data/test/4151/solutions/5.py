
n = int(input())

L = [int(x) for x in input().split()]

D = {}

for i in L:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
        
P = {}

for i in range(n):
    P[L[i]] = i

ans = 1
index = 0
for i in range(n):
    if i <= index:
        if D[L[i]] > 1:
            index = max(P[L[i]],index)
    else:
        ans *= 2
        ans = ans % 998244353
        index = P[L[i]]

print(ans)

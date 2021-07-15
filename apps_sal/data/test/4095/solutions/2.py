T = input().split(' ')
n = int(T[0])
m = int(T[1])
S = input().split(' ')
for i in range(n):
    S[i] = int(S[i])
ind = 0
for k in range(n):
    if S[k] == m:
        ind = k
k = ind
P = [0]*(n+1)
N = [0]*(n+1)
R = [0]*(n-k)
L = [0]*(k+1)
for i in range(k):
    if S[k-1-i] < m:
        L[k-1-i] = L[k-i] - 1
    else:
        L[k-1-i] = L[k-i] + 1
for i in range(n-k-1):
    if S[k+1+i] > m:
        R[1+i] = R[i] + 1
    else:
        R[1+i] = R[i] - 1
c = 0
for el in R:
    if el >= 0:
        P[el]+=1
        if el == 0:
            N[el]+=1
    else:
        N[-el]+=1
for el in L:
    if el >= 1:
        c = c + N[el] + N[el-1]
    else:
        c = c + P[-el] + P[-el+1]
print(c)


import sys

N = int(input())
S = input()

W = [0]*N
E = [0]*N
ans = N
for i in range(1, N):
    W[i] = W[i-1]+1 if S[i-1]=='W' else W[i-1]
    E[-i-1] = E[-i]+1 if S[-i]=='E' else E[-i]

for i in range(N):
    ans = min(W[i]+E[i], ans)

print(ans)





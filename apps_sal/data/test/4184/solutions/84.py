N = int(input())
W = [int(i) for i in input().split()]
S = 0
for i in range(N):
    S += W[i]
ans = 99999

for i in range(1,N+1):
    S1 = 0
    for j in range(i):
        S1 += W[j]
    S2 = S - S1
    ans = min(ans,abs(S1-S2))

print(ans)


N, M , K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

RA = [0]
RB = [0]

tmp = 0
for i in range(N):
    tmp += A[i]
    RA.append(tmp)

tmp = 0
for i in range(M):
    tmp += B[i]
    RB.append(tmp)
#print(RA)
#print(RB)

ans = 0
best = M
for i in range(N+1):
    if RA[i]>K:
        break
    while RB[best] > K - RA[i]:
        best -= 1
    ans = max(ans, i + best)

print(ans)


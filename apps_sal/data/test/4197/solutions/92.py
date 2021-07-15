N = int(input())
A = list(map(int, input().split()))
L = [[] for x in range(N)]

for i in range(N):
    L[i] = [A[i], i+1]
L.sort()

ANS = [0 for i in range(N)]
for i in range(N):
    ANS[i] = L[i][1]
print(*ANS)

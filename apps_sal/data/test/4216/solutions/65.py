import math
N = int(input())

L = []
for i in range(1, math.floor(N ** 0.5) + 1):
    if N % i == 0:
        L.append([i, N // i])

ans = float('inf')
for i in range(len(L)):
    if L[i][0] > L[i][1]:
        ans = min(ans, len(str(L[i][0])))
    else:
        ans = min(ans, len(str(L[i][1])))

print(ans)

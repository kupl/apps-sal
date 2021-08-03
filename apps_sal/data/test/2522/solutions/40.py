from collections import Counter
import sys
import random

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ca = Counter(A)
cb = Counter(B)
for i in range(N + 1):
    if ca[i] + cb[i] > N:
        print('No')
        return

C = [0] * (N + 1)
D = [0] * (N + 1)

for i in range(N):
    C[i + 1] += C[i] + ca[i + 1]
    D[i + 1] += D[i] + cb[i + 1]

x = 0

for i in range(N):
    x = max(x, C[i + 1] - D[i])

ans = [B[(i - x) % N] for i in range(N)]

print('Yes')
print(*ans)

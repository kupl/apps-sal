import math
N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] * (N + 1)
s = 0
for i in reversed(range(1, N + 1)):
    ball = 0
    for j in range(i, N + 1, i):
        ball += B[j]
    if ball % 2 != A[i]:
        B[i] = 1
        s += 1

print(s)
print(*[i for i, b in enumerate(B) if b == 1], sep=' ')

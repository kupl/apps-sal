import math
n = int(input())
Y = [0.0]
Z = [0.0]
Y = Y + [float(y) for y in input().split()]
Z = Z + [float(z) for z in input().split()]
S = [y + z for (y, z) in zip(Y, Z)]
CS = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    CS[i] = CS[i - 1] + S[i]
A = [0 for i in range(0, n + 1)]
B = [0 for i in range(0, n + 1)]
CA = 0
for e in range(1, n + 1):
    dis = (CS[e] - 2 * CA) ** 2 + 4 * (S[e] * CA - Y[e])
    if abs(dis) < 1e-12:
        dis = 0
    A[e] = CS[e] - 2 * CA + math.sqrt(dis)
    A[e] /= 2
    CA += A[e]
    B[e] = S[e] - A[e]
print(' '.join(['%.7f' % a for a in A[1:]]))
print(' '.join(['%.7f' % a for a in B[1:]]))

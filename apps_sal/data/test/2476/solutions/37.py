N = int(input())
A = list(map(int,input().split()))
C = [0] * (N + 1)
for a in A:
    C[a] += 1
D = [0] * (N + 1)
for c in C:
    D[c] += 1
P = [0] * (N + 1)
Q = [0] * (N + 1)
for i in range(1, N+1):
    P[i] = P[i-1] + i * D[i]
    Q[i] = Q[i-1] + D[i]
F = [0] * (N + 1)
for i in range(1, N+1):
    F[i] = int((P[i] + i * (Q[N] - Q[i])) / i)
index = N
for i in range(1, N+1):
    while True:
        if index == 0:
            print(0)
            break
        if F[index] >= i:
            print(index)
            break
        else:
            index -= 1

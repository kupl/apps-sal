N, M = list(map(int, input().split()))
L = [0] * (N + 1)
for i in range(M):
    A, B = list(map(int, input().split()))
    L[A] += 1
    L[B] += 1
for j in range(1, N + 1):
    print((L[j]))

n = int(input())
A = list(map(int, input().split()))
P = [0] * n
for i in range(n):
    P[A[i] - 1] = i + 1
print(*P, sep=' ')

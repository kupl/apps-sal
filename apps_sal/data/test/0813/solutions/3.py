(n, a, b) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
used = [0] * n
for i in range(a):
    used[A[i] - 1] = 1
for i in range(b):
    if used[B[i] - 1] == 0:
        used[B[i] - 1] = 2
print(*used)

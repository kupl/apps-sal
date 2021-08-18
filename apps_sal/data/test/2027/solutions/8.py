n = int(input())
L = list(map(int, input().split()))
R = [0 for _ in range(n)]
R[n - 1] = L[n - 1]
t = L[n - 1]
for i in range(n - 2, -1, -1):
    if 1:
        R[i] = L[i] + t
        t = R[i] - t
for i in range(n):
    print(R[i], end=" ")

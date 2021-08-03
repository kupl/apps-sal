n = int(input())
A = list(map(int, input().split()))
L = [0] * n
for i in range(n - 1):
    L[A[i] - 1] += 1
for l in L:
    print(l)

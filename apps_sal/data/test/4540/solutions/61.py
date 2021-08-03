N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)
x = 0
for i in range(0, N + 1):
    x += abs(A[i + 1] - A[i])
for i in range(1, N + 1):
    print((x - abs(A[i] - A[i - 1]) - abs(A[i] - A[i + 1]) + abs(A[i + 1] - A[i - 1])))

N = int(input())
A = list(map(int, input().split()))
cost = abs(A[0])
for i in range(1, N):
    cost += abs(A[i] - A[i - 1])
cost += abs(A[N - 1])
prev = 0
A.append(0)
for i in range(N):
    x = abs(A[i + 1] - prev)
    y = abs(A[i] - prev) + abs(A[i + 1] - A[i])
    print(cost - (y - x))
    prev = A[i]

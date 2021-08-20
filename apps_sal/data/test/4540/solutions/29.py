n = int(input())
A = [0] + list(map(int, input().split())) + [0]
ans = 0
for i in range(n + 1):
    ans += abs(A[i + 1] - A[i])
for i in range(1, n + 1):
    print(ans - abs(A[i] - A[i - 1]) - abs(A[i + 1] - A[i]) + abs(A[i + 1] - A[i - 1]))

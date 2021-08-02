n = int(input())
A = [0] + list(map(int, input().split())) + [0]

cost = 0
for i in range(n + 1):
    cost += abs(A[i] - A[i + 1])

for i in range(1, n + 1):
    ans = cost
    ans -= abs(A[i] - A[i - 1])
    ans -= abs(A[i] - A[i + 1])
    ans += abs(A[i - 1] - A[i + 1])
    print(ans)

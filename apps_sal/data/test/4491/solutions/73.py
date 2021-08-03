N = int(input())
A = list([0] * N for _ in range(2))
for i in range(2):
    A[i] = list(map(int, input().split()))

result = []

for i in range(N):
    tmp = 0
    tmp += sum(A[0][0:i + 1])
    tmp += sum(A[1][i:N])
    result.append(tmp)

print(max(result))

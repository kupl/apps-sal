N = int(input())
A = list(map(int, input().split()))
m = [abs(0 - A[0])] * (N + 1)
for i in range(1, N):
    m[i] = abs(A[i] - A[i - 1])
m[-1] = abs(0 - A[-1])
a = sum(m)
A.append(0)
for i in range(N):
    print(a + abs(A[i - 1] - A[i + 1]) - (abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1])))

N = int(input())
A = list(map(int, input().split()))
A = A * 2

s = [0] * (2 * N)
s[0] = A[0]
s[1] = A[1]

for i in range(2, 2 * N):
    s[i] = s[i - 2] + A[i]
s.append(0)
ss = s[2 * N - 1]

for i in range(N):
    print(ss - 2 * (s[i + N - 2] - s[i - 1]), end=" ")

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
    d = min(A[i], B[i])
    A[i] -= d
    B[i] -= d
    res += d
    d = min(A[i + 1], B[i])
    A[i + 1] -= d
    res += d

print(res)

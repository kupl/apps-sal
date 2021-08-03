n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(n):
    d = min(A[i], B[i])
    cnt += d
    A[i] -= d
    B[i] -= d
    d = min(A[i + 1], B[i])
    cnt += d
    A[i + 1] -= d

print(cnt)

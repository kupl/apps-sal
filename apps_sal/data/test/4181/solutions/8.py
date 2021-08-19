N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    c = min(A[i] + A[i + 1], B[i])
    cnt += c
    A[i + 1] = A[i + 1] - max(c - A[i], 0)
print(cnt)

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

now = 1

while K:
    if K & 1:
        now = A[now]
    A = [A[A[i]] for i in range(len(A))]
    K >>= 1

print(now)

(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * n
B[0] = A[0]
for i in range(1, n):
    B[i] = max(A[i], k - B[i - 1])
print(sum(B) - sum(A))
print(' '.join(list(map(str, B))))

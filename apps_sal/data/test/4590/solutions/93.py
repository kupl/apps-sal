(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
(A, B) = ([0], [0])
for i in range(n):
    A.append(A[i] + a[i])
for i in range(m):
    B.append(B[i] + b[i])
(ans, j) = (0, m)
for i in range(n + 1):
    if A[i] > k:
        break
    while B[j] > k - A[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)

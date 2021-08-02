def R(): return list(map(int, input().split()))


n, k1, k2 = R()
k = k1 + k2
A = list(R())
B = tuple(R())
for i in range(n):
    A[i] = abs(A[i] - B[i])
for _ in range(k):
    idx = A.index(max(A))
    A[idx] = abs(A[idx] - 1)
s = 0
for a in A:
    s += a * a
print(s)

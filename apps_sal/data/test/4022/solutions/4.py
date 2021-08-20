N = int(input())
A = [None] * N
for i in range(N):
    A[i] = list(map(int, input().split()))
A.sort(key=lambda x: x[1])
left = sorted(A)
right = sorted(A[::-1], key=lambda x: x[1])
X = left[:N - 1]
Y = right[1:]
aa = min(X, key=lambda x: x[1])[1] - max(X)[0]
bb = min(Y, key=lambda x: x[1])[1] - max(Y)[0]
print(max(aa, bb, 0))

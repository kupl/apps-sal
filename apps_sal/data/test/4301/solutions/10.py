N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

mx = max(A)
mxidx = A.index(mx)

for i in range(N):
    if i == mxidx:
        B = A[0:i] + A[i + 1:N]
        print(max(B))
    else:
        print(mx)

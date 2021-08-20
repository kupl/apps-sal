N = int(input())
(A, B) = ([], [])
for i in range(N):
    (a, b) = map(int, input().split())
    A.append(a)
    B.append(b)
(A, B) = map(sorted, (A, B))
if N % 2 == 1:
    (mA, mB) = (A[N // 2], B[N // 2])
    print(mB - mA + 1)
else:
    (mA, mB) = ((A[N // 2 - 1] + A[N // 2]) / 2, (B[N // 2 - 1] + B[N // 2]) / 2)
    print(int((mB - mA) / 0.5 + 0.5) + 1)

N = int(input())
A = []
B = []
for _ in range(N):
    (x, y) = map(int, input().split())
    A.append(x + y)
    B.append(x - y)
A = sorted(A)
B = sorted(B)
print(max(A[-1] - A[0], B[-1] - A[0], A[-1] - A[0], B[-1] - B[0]))

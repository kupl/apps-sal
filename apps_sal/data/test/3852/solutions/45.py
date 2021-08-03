"""
まずは、全部正の数にするか、負の数にする
"""
N = int(input())
A = list(map(int, input().split()))
print((2 * N - 1))
if abs(max(A)) >= abs(min(A)):
    idx = A.index(max(A)) + 1
    for i in range(1, N + 1):
        print((idx, i))
    for i in range(1, N):
        print((i, i + 1))
else:
    idx = A.index(min(A)) + 1
    for i in range(1, N + 1):
        print((idx, i))
    for i in range(N, 1, -1):
        print((i, i - 1))

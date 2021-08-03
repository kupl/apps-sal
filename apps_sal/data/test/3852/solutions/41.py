n = int(input())
A = list(map(int, input().split()))
M = max(A)
m = min(A)
M_idx = A.index(M) + 1
m_idx = A.index(m) + 1
print(2 * n - 1)
if abs(M) >= abs(m):
    for i in range(1, n + 1):
        print(M_idx, i)
    for i in range(1, n):
        print(i, i + 1)
else:
    for i in range(1, n + 1):
        print(m_idx, i)
    for i in range(n - 1, 0, -1):
        print(i + 1, i)

(n, s) = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(n)]
T = [s - k for k in range(s + 1)]
for A in L:
    T[A[0]] = max([T[A[0]], A[1]])
r = 0
for k in range(s, 0, -1):
    r = max([r, T[k]])
    r += 1
print(r)

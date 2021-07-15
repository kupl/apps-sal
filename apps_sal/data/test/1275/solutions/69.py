N, K = map(int, input().split())
ans = 0
for B in range(2, 2*N+1):
    A = K + B
    if A < 2 or A > 2*N:
        continue
    a_n = min(A-1, 2*N + 1 - A)
    b_n = min(B-1, 2*N + 1 - B)
    ans += a_n * b_n

print(ans)

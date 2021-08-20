def solve(d, A):
    if d == 100:
        return 0
    B = [0] * 101
    for a in A:
        B[a] += 1
    for i in range(1, 101):
        B[i] += B[i - 1]
    M = 0
    for i in range(d + 1, 101):
        u = B[i] - B[i - d - 1]
        M = max(u, M)
    return len(A) - M


(n, d) = map(int, input().split())
a = list(map(int, input().split()))
print(solve(d, a))

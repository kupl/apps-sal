N = ~-int(input())
C = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    p, q, r = C[i]
    A = q + p
    for j in range(i + 1, N):
        c, s, f = C[j]
        if A < s:
            A = s
        m = (A - s) % f
        if m != 0:
            A += f - m
        A += c
    print(A)
print(0)

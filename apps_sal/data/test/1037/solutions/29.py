N = int(input())
A = list(map(int, input().split()))
A = sorted([(val, pos) for (pos, val) in enumerate(A)], reverse=True)
dp = [0]
for (i, (val, pos)) in enumerate(A):
    ldp = [e + val * abs(pos - (i - r)) for (r, e) in enumerate(dp)]
    rdp = [e + val * abs(N - 1 - r - pos) for (r, e) in enumerate(dp)]
    dp = [max(L, R) for (L, R) in zip(ldp + [0], [0] + rdp)]
print(max(dp))

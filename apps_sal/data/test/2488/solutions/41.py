import bisect
(N, D, A) = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
C = sorted(B)
(d, E) = zip(*C)
Damage = [0] * N
for i in range(N):
    e = bisect.bisect_right(d, d[i] + 2 * D)
    Damage[i] = e
dd = [0] * (N + 1)
cnt = 0
for i in range(N):
    if i != 0:
        dd[i] += dd[i - 1]
    h = E[i]
    h -= dd[i]
    if h > 0:
        bomb = -(-h // A)
        cnt += bomb
        dd[i] += A * bomb
        dd[Damage[i]] -= A * bomb
print(cnt)

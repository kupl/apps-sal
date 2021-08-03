N, A, B = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]
ok = 10**9
ng = 0
while ng + 1 < ok:
    c = ok + ng >> 1
    G = [max(0, h - c * B) for h in H]
    n = sum(-(-g // (A - B)) for g in G)
    if c >= n:
        ok = c
    else:
        ng = c
print(ok)

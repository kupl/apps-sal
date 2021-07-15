import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    TLR = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, M, TLR))


for N, M, TLR in Query:
    TLR.sort()
    large = M
    small = M
    pret = 0
    ok = True
    for t, l, r in TLR:
        delta = t - pret
        large += delta
        small -= delta

        if large < l or r < small:
            ok = False
            break
        large = min(large, r)
        small = max(small, l)

        pret = t
    
    print("YES" if ok else "NO")

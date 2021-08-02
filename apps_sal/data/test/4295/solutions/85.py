N, K = map(int, input().split())
residue = N % K
if residue * 2 < K:
    print(residue)
else:
    print(K - residue)

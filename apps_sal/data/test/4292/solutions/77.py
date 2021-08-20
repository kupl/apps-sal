(N, K) = map(int, input().split())
P = list(map(int, input().split()))
assert len(P) == N
P = sorted(P)
print(sum(P[:K]))

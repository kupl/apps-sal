N, K = map(int, input().split())
P = list(map(int, input().split()))
assert len(P) == N
# 1 <= K <= N <= 1000
P = sorted(P)
print(sum(P[:K]))

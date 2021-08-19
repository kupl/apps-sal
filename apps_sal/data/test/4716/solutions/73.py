(N, K) = list(map(int, input().split()))
S = list(map(int, input().split()))
S = sorted(S, reverse=True)
print(sum(S[:K]))

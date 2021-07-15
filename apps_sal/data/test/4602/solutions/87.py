with open(0) as f:
    N, K, *X = map(int, f.read().split())
print(2*sum(min(x, K-x) for x in X))

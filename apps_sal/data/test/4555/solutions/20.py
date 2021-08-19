(a, b, k) = map(int, input().split())
X = range(a, b + 1)
Y = sorted(list(set(X[:k]) | set(X[-k:])))
print(*Y, sep='\n')

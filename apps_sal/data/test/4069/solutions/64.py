(X, K, D) = map(int, input().split())
X = abs(X) - K % 2 * D
E = D * 2
print(max(min(X % E, -X % E), X - D * (K - K % 2)))

N, M, x, y = map(int, input().split())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

l = max(X)
r = min(Y)

print('No War' if l < r and not (y <= l or r <= x) else 'War')

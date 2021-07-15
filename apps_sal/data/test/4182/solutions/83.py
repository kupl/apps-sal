N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(['No War', 'War'][max(x + [X]) >= min(y + [Y])])

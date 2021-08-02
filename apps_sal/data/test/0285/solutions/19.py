n = int(input())
X, Y = input().split()
X, Y = float(X) + 1e-10, float(Y) - 1e-10
L = [list(map(float, input().split())) for _ in range(n)]
print('NO' if [i for x, i in sorted((k * X + b, i) for i, (k, b) in enumerate(L))] == [i for x, i in sorted((k * Y + b, i) for i, (k, b) in enumerate(L))] else 'YES')

N, M, X, Y = map(int, input().split())
x = [int(s) for s in input().split()]
y = [int(s) for s in input().split()]
x.append(X)
y.append(Y)
print('No War') if max(x) < min(y) else print('War')

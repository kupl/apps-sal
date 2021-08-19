(n, m, x, y) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.append(x)
Y.append(y)
if min(Y) - max(X) >= 1:
    print('No War')
else:
    print('War')

(n, m, x, y) = list(map(int, input().split()))
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
xs.append(x)
ys.append(y)
if max(xs) < min(ys):
    print('No War')
else:
    print('War')

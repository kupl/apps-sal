n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
if x[n - 1] < Y and X < y[0] and x[n - 1] < y[0]:
    print('No War')
else:
    print('War')

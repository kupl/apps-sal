N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_max = max(x)
z = min(y)

if X < z <= Y and x_max < z:
    print('No War')
else:
    print('War')

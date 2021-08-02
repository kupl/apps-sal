n, m, X, Y = list(map(int, input().split()))
x = list(map(int, input().split())) + [X]
y = list(map(int, input().split())) + [Y]
if min(y) - max(x) >= 1:
    print('No War')
else:
    print('War')

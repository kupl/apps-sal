(N, M, X, Y) = list(map(int, input().split()))
x = list(map(int, input().split())) + [X]
y = list(map(int, input().split())) + [Y]
if max(x) < min(y):
    print('No War')
else:
    print('War')

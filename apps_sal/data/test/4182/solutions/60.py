(N, M, X, Y) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
if X <= x[-1] and x[-1] < y[0] and (y[0] <= Y):
    print('No War')
else:
    print('War')

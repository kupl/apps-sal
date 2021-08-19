(N, M, X, Y) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
sx = sorted(x)
sy = sorted(y)
if sx[-1] < sy[0] and X < sy[0] and (sx[-1] < Y):
    print('No War')
else:
    print('War')

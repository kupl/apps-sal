(N, M, X, Y) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if max(x) < min(y) and X < max(x) <= Y and (X < min(y) <= Y):
    print('No War')
else:
    print('War')

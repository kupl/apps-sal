N, M, X, Y = list(map(int, input().split()))
x = sorted(list(map(int, input().split())))
y = sorted(list(map(int, input().split())))

if X < Y and x[-1] < Y and X < y[0] and x[-1] < y[0] :
    print('No War')
else:
    print('War')


N, M, X, Y = map(int, input().split())
lx = [int(x) for x in input().split()]
lx.append(X)
ly = [int(y) for y in input().split()]
ly.append(Y)
if X >= Y or max(lx) >= min(ly):
    print('War')
else:
    print('No War')

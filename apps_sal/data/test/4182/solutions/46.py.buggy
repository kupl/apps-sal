N, M, X, Y = map(int, input().split())
xx = list(map(int, input().split()))
yy = list(map(int, input().split()))

xx.sort()
yy.sort()


for Z in range(X + 1, Y):
    if Z > xx[-1] and yy[0] >= Z:
        print('No War')
        return

print('War')

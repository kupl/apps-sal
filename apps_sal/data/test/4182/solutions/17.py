n, m, x, y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))
lx.append(x)
ly.append(y)
lx.sort()
ly.sort()

if lx[-1] < ly[0]:
    print('No War')
else:
    print('War')

n = int(input())
xlevels = list()
ylevels = list()
xlevels[:] = list(map(int, input().split(' ')))
ylevels[:] = list(map(int, input().split(' ')))
xlevels = xlevels[1:len(xlevels)]
ylevels = ylevels[1:len(ylevels)]
levels = list()
levels = set(xlevels[:]) | set(ylevels[:])
if len(levels) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

n, m = map(int, input().split())

xx = sorted(list(map(int, input().split())))

yy = [abs(xx[i] - xx[i + 1]) for i in range(m - 1)]

sy = sorted(yy)

if n > 1:
    print(sum(sy[:-n + 1]))
else:
    print(xx[-1] - xx[0])

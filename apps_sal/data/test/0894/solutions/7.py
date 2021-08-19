def solve(x, y):
    t = abs(x) + abs(y)
    if x > 0 and y > 0:
        return (0, t, t, 0)
    elif x > 0 and y < 0:
        return (0, -t, t, 0)
    elif x < 0 and y > 0:
        return (-t, 0, 0, t)
    else:
        return (-t, 0, 0, -t)


def test():
    assert solve(10, 5) == (0, 15, 15, 0)
    assert solve(-10, 5) == (-15, 0, 0, 15)
    print('test passes')


tmp = input()
tmp = list(map(int, tmp.split()))
for i in solve(tmp[0], tmp[1]):
    print(i, end=' ')

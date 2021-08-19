(n, m) = map(int, input().split())
xyz = [list(map(int, input().split())) for _i in range(n)]
r = []
for i in range(2 ** 3):
    checker = []
    num = i
    for _i in range(3):
        if num % 2 == 1:
            checker.append(1)
        else:
            checker.append(-1)
        num >>= 1
    _xyz = []
    for j in range(n):
        _abc = [checker[s] * xyz[j][s] for s in range(3)]
        _xyz.append([sum(_abc)] + _abc)
    _xyz.sort(reverse=True)
    _r = abs(sum((i[1] for i in _xyz[:m]))) + abs(sum((i[2] for i in _xyz[:m]))) + abs(sum((i[3] for i in _xyz[:m])))
    r.append(_r)
print(max(r))

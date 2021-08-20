def solve(n, m, b):
    b = [1] + b
    s = 0
    for i in range(m):
        s += (b[i + 1] - b[i] + n) % n
    return s


def test():
    assert solve(4, 3, [3, 2, 3]) == 6
    assert solve(4, 3, [2, 3, 3]) == 2
    print('test passes')


tmp = input()
(n, m) = list(map(int, tmp.split()))
tmp = input()
b = list(map(int, tmp.split()))
print(solve(n, m, b))

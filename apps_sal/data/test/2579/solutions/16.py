3


def read_ints():
    return [int(i) for i in input().split()]


l, r, x, y, k = read_ints()

if x * k <= r and y * k >= l and l // k + (l % k > 0) <= r // k:
    print('YES')
else:
    print('NO')

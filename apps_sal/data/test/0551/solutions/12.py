n = input()
y = list(map(int, input().split()))


def chk(limit):
    return len(set(2 * yi - limit * i for i, yi in enumerate(y))) == 2


s = 2 * (y[1] - y[0]), 2 * (y[2] - y[1]), y[2] - y[0]

print('Yes' if any(chk(x) for x in s) else 'No')


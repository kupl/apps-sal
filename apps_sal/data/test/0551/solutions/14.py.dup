n = int(input())
y = list(map(int, input().split()))


def check(d):
    return len(set(2 * yi - d * i for i, yi in enumerate(y))) == 2


print('Yes' if any(check(d) for d in [2 * (y[1] - y[0]), 2 * (y[2] - y[1]), y[2] - y[0]]) else 'No')

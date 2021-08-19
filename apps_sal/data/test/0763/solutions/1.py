def d(x, i, a):
    return 2 * a * (abs(x - i) + abs(i - 1) + abs(1 - x))


n = int(input())
arr = [int(k) for k in input().split()]


def e(x):
    return sum((d(x, i + 1, a) for (i, a) in enumerate(arr)))


print(min((e(x) for x in range(1, n + 1))))

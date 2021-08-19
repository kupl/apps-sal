n = int(input())

A = [int(x) for x in input().split()]


def cost(x):
    res = 0
    for i, a in enumerate(A):
        # Down:
        res += (abs(x - i) + abs(i - 0) + abs(x - 0)) * a

        # Up:
        res += (abs(x - 0) + abs(0 - i) + abs(i - x)) * a

    return res


print(min(cost(x) for x in range(len(A))))

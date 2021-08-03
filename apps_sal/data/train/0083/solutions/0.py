def one():
    return int(input())


def two():
    return list(map(int, input().split()))


def lis():
    return list(map(int, input().split()))


def st():
    return input()


for _ in range(one()):
    x, y, a, b = list(map(int, input().split()))
    d = y - x
    if d % (a + b) == 0:
        print(d // (a + b))
    else:
        print(-1)

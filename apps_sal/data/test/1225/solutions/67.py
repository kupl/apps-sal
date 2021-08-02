h = int(input())


def cal(x):
    if x == 1: return 1
    return cal(x // 2) * 2 + 1


print(cal(h))

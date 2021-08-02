n = int(input())


def p(x):
    if x == 2:
        return True
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True


for i in range(n, 2 * n):
    if p(i):
        print(i)
        break

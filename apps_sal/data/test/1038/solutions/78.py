(A, B) = map(int, input().split())


def f(X):
    a = 1
    temp = 2
    ret = []
    while a > 0:
        (a, b) = divmod(X + 1, temp)
        if temp == 2:
            ret.append(a % 2)
        else:
            ret.append(max(b - temp // 2, 0) % 2)
        temp *= 2
    return ''.join(map(str, reversed(ret)))


print(int(f(max(0, A - 1)), 2) ^ int(f(B), 2))

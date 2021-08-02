def check(n, D):
    N = []
    while n != 0:
        N.append(n % 10)
        n //= 10
    for d in D:
        if d in N:
            return False
    return True


def __starting_point():
    n, k = [int(x) for x in input().split(' ')]
    D = [int(x) for x in input().split(' ')]
    res = n
    while True:
        if check(res, D):
            break
        else:
            res += 1
    print(res)


__starting_point()

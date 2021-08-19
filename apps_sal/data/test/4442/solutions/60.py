(a, b) = map(int, input().split())


def ans152(a: int, b: int):
    listab = [str(a) * b, str(b) * a]
    listab.sort()
    return int(listab[0])


print(ans152(a, b))

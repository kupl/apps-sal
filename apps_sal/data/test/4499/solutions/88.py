a, b, c = input().split()


def answer(a: str, b: str, c: str) -> str:
    return ((a[0] + b[0] + c[0]).upper())


print((answer(a, b, c)))

a, b, c, d = list(map(int, input().split()))


def answer(a: int, b: int, c: int, d: int) -> str:
    if (c + b - 1) // b <= (a + d - 1) // d:
        return 'Yes'
    else:
        return 'No'


print((answer(a, b, c, d)))

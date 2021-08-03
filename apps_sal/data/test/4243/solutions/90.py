x = int(input())


def answer(x: int) -> int:
    ans = 1000 * (x // 500)
    x %= 500
    ans += 5 * ((x - 500 * (x // 500)) // 5)
    return ans


print(answer(x))

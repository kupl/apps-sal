n, m, x = map(int, input().split())
a = list(map(int, input().split()))


def answer(n: int, m: int, x: int, a: list) -> int:
    left = 0
    right = 0
    for i in a:
        if i < x:
            left += 1
        else:
            right += 1
    return min(left, right)


print(answer(n, m, x, a))

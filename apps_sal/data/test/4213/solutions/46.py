n = int(input())
a = list(map(int, input().split()))


def answer(n: int, a: list) -> int:
    return max(a) - min(a)


print(answer(n, a))

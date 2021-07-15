k, x = list(map(int, input().split()))


def answer(k: int, x: int) -> str:
    answer = []
    for i in range((x - (k - 1)), (x + k)):
        answer.append(i)
    return " ".join(map(str, answer))

print((answer(k, x)))



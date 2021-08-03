c1, c2 = [input() for _ in range(2)]


def answer(c1: str, c2: str) -> str:
    if c1[0] == c2[2] and c1[2] == c2[0] and c1[1] == c2[1]:
        return 'YES'
    else:
        return 'NO'


print(answer(c1, c2))

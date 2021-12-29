import numpy as np


def main() -> None:
    (n, m, x) = list(map(int, input().split()))
    books = [tuple(map(int, input().split())) for _ in range(n)]
    is_able = False
    answer = float('inf')
    for i in range(2 ** n):
        money = 0
        skills = np.zeros(m)
        for j in range(n):
            if i >> j & 1:
                money += books[j][0]
                skills += books[j][1:]
        if x <= skills.min():
            is_able = True
            answer = min(answer, money)
    print(answer if is_able else -1)
    return


def __starting_point():
    main()


__starting_point()

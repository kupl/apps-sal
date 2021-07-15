from typing import List


def answer(a: List[List[int]], n: int, b: List[int]) -> str:
    bingo_card = list([i[j] in b for i in a] for j in range(3))
    for i in range(2):
        for j in bingo_card:
            if all(j):
                return 'Yes'
        if i == 0:
            bingo_card = list(zip(*bingo_card))

    if bingo_card[0][0] and bingo_card[1][1] and bingo_card[2][2]:
        return 'Yes'
    if bingo_card[0][2] and bingo_card[1][1] and bingo_card[2][0]:
        return 'Yes'

    return 'No'


def main():
    a = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b = list(int(input()) for _ in range(n))
    print(answer(a, n, b))


def __starting_point():
    main()
__starting_point()

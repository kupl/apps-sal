(r1, c1, r2, c2) = map(int, input().split())


def rookMoves():
    return 1 if r1 == r2 or c1 == c2 else 2


def bishopMoves():
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        return 0
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        return 1
    return 2


def kingMoves():
    return max(abs(r1 - r2), abs(c1 - c2))


print(rookMoves(), bishopMoves(), kingMoves())

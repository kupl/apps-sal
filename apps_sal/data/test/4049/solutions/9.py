def count_wins(a1, a2, a3, b1, b2, b3):
    return min(a1, b2) + min(a2, b3) + min(a3, b1)


def solve_e(a1, a2, a3, b1, b2, b3):
    wins = count_wins(a1, a2, a3, b1, b2, b3)
    loses = max(0, a1 - b1 - b3) + max(0, a2 - b2 - b1) + max(0, a3 - b2 - b3)
    return (loses, wins)


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*solve_e(*a, *b))

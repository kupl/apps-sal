from math import factorial


def choose(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


def allPossibilities(balls):
    n = sum(balls)
    total = factorial(n)
    for b in balls:
        total //= factorial(b)
    return total


def count(balls, balance, a, b, i):
    c = balls[i]
    upper = min(c, a)
    lower = max(c - b, 0)
    tempBalance = balance
    total = 0
    for j in range(lower, upper + 1):
        balance = tempBalance
        if j == 0:
            balance -= 1
        if j == c:
            balance += 1
        if i == len(balls) - 1:
            if balance == 0:
                return 1
            else:
                return 0
        else:
            total += choose(a, j) * choose(b, c - j) * count(balls, balance, a - j, b - c + j, i + 1)
    return total


class Solution:

    def getProbability(self, balls: List[int]) -> float:
        return count(balls, 0, sum(balls) // 2, sum(balls) // 2, 0) / allPossibilities(balls)

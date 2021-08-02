from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()
vals = lm()

avals = [abs(v) for v in vals]

avals.sort()


total = 0

start = 0

end = 1


while end < n:

    if 2 * avals[start] >= avals[end]:
        end += 1

    else:

        total = total + max(0, end - start - 1)
        start += 1


num = end - start

total += num * (num - 1) // 2


print(total)

"""input
6 1
5 1 2 3 4 1
"""


def rints():
    return list(map(int, input().split()))


def ri():
    return int(input())


MAX_A = 10 ** 5
(n, x) = rints()
arr = rints()
seen = [0] * (MAX_A + 1)
count = 0
for elem in arr:
    partner = x ^ elem
    if partner <= MAX_A:
        count += seen[partner]
    seen[elem] += 1
print(count)

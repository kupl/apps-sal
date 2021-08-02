import math


def solve(n):
    if n == 2:
        return 3
    bad = [1, 1, 5, 1, 21, 1, 85, 73, 341, 89, 1365, 1, 5461, 4681, 21845, 1, 87381, 1, 349525, 299593, 1398101, 178481, 5592405, 1082401]
    if 2 ** math.floor(math.log2(n)) <= n <= 2 ** (math.floor(math.log2(n)) + 1) - 2:
        return (2 ** math.ceil(math.log2(n)) - 1)
    else:
        return bad[math.floor(math.log2(n)) - 1]


q = int(input())
for i in range(q):
    print(solve(int(input())))

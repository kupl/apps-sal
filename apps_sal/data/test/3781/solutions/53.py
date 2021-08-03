from collections import Counter


def solve(a):
    c = Counter(a)

    res = True

    for i in list(c.values()):
        if i % 2 != 0:
            res = False

    if N % 2 == 0:
        if res:
            return "Second"
        else:
            return "First"
    else:
        return "Second"


T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print((solve(a)))

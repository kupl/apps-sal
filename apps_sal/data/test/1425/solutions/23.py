from collections import deque

# from itertools import permutations
# from random import *

n = int(input())
a = sorted(map(int, input().strip().split()))


def solve(a):
    d = deque()
    test = 0
    for i in a:
        if test:
            d.appendleft(i)
            test = 0
        else:
            d.append(i)
            test = 1

    d = list(d)
    # print(d)

    if all(a < b + c for a, b, c in zip(d, d[1:] + [d[0]], [d[-1]] + d)):
        print("YES")
        print(*d)
        # return True
    else:
        print("NO")
        # return False

# def brute(a):
#     for d in permutations(a):
#         if all(a < b + c for a, b, c in zip(d, d[1:] + (d[0],), (d[-1],) + d)):
#             print(d)
#             return True
#     return False


solve(a)

# while True:
# a = sorted([randint(2, 10) for _ in range(5)])
# if solve(a) != brute(a):
# print(a)
# else:
# print("ok")

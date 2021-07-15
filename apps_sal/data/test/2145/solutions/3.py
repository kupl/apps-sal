import random


def get_many_ints():
    return list(map(int, input().split()))


def get_int():
    return int(input())


def get_int_list():
    return list(get_many_ints())


def prog():
    x, y = get_many_ints()
    if x >= 4:
        print("YES")
        return
    ok = (x == 1 and y == 1) or (x in [2, 3] and y <= 3)
    print("YES" if ok else "NO")


q = get_int()
for _ in range(q):
    prog()


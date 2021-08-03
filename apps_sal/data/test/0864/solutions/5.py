from collections import Counter

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

C = Counter(a)


def check(p):
    return sum(el // p for el in list(C.values())) >= n


def binSearch(a, b):
    left, right = a - 1, b + 1

    while right - left > 1:
        mid = (left + right) // 2

        if check(mid):
            left = mid

        else:
            right = mid

    return left


print(binSearch(1, 100))

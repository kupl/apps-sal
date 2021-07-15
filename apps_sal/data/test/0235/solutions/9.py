n = int(input())


def check(p):
    V = 0
    n_ = n
    while n_ > 0:
        temp = min(n_, p)
        V += temp
        n_ -= temp
        n_ -= n_ // 10

    return 2 * V >= n


def binSearch(a, b):
    left, right = a - 1, b + 1

    while right - left > 1:
        mid = (left + right) // 2

        if check(mid):
            right = mid

        else:
            left = mid

    return right


print(binSearch(1, n // 2))


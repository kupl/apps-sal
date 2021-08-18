n, k, A, B = list(map(int, input().split()))
n = 2 ** n
a = list(sorted(list(map(int, input().split()))))


def recurs(start, end, array):
    if len(array) == 0:
        return A
    if end - start == 1:
        return B * len(array)

    middle = (start + end) // 2
    c, d = [], []
    for x in array:
        if x < middle:
            c += [x]
        else:
            d += [x]
    return min(B * len(array) * (end - start), recurs(start, middle, c) + recurs(middle, end, d))


print(recurs(1, n + 1, a))

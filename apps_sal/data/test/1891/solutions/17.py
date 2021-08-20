(n, k, A, B) = list(map(int, input().split()))
n = 2 ** n
a = sorted(list(map(int, input().split())))


def recurs(start, end, sum_all, array):
    if sum_all == 0:
        return A
    else:
        energy = B * (end - start) * sum_all
    if end - start == 1:
        return energy
    (c, d) = ([], [])
    for x in array:
        if x < (start + end) // 2:
            c += [x]
        else:
            d += [x]
    first = len(c)
    second = sum_all - first
    tmp = recurs(start, (start + end) // 2, first, c)
    tmp += recurs((start + end) // 2, end, second, d)
    return (energy < tmp) * energy + (1 - (energy < tmp)) * tmp


print(recurs(1, n + 1, k, a))

(n, k) = [int(s) for s in input().split()]
lengths = [1]
(n, k) = (n - 1, k - 1)
for i in range(n):
    lengths.append(lengths[-1] * 2 + 1)


def search(n, k):
    if k == 0:
        return 1
    l = lengths[n]
    if k == l // 2:
        return n + 1
    if k < l // 2:
        return search(n - 1, k)
    else:
        return search(n - 1, k - l // 2 - 1)


print(search(n, k))

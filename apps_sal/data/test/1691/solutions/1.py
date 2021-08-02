

def __starting_point():
    n, k = list(map(int, input().strip().split()))

    if k > n // 2:
        k = n - k

    intersection = n * [0]

    count = 1

    done = False
    i = 0
    result = []
    for i in range(1, n + 1):
        nn = (i * k) // n
        j = (i * k) % n
        if j < k:
            count += (2 * nn)
        else:
            count += (2 * nn + 1)
        result.append(count)

    result[-1] -= 1
    print(" ".join([str(r) for r in result]))


__starting_point()

def readinput():
    n, k = list(map(int, input().split()))
    return n, k


def main(n, k):
    m = n // k
    count = m * m * m
    if k % 2 == 0:
        m = (n + k // 2) // k
        count += m * m * m
    return count


def __starting_point():
    n, k = readinput()
    ans = main(n, k)
    print(ans)


__starting_point()

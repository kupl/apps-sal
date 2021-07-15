def key(ab):
    a, b = ab
    return a - b


def main():
    n = int(input())
    nm = 0
    m1 = n - 1
    res = 0
    for a, b in sorted((tuple(map(int, input().split())) for _ in range(n)), key=key):
        res += a * m1 + b * nm
        nm += 1
        m1 -= 1
    print(res)


main()


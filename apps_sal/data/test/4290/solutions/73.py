def main():
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            cnt += 1

    for i in range(m):
        for j in range(i + 1, m):
            cnt += 1
    return cnt


def __starting_point():
    print(main())


__starting_point()

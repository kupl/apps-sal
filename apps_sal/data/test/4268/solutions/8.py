def main():
    n, d = map(int, input().split())
    ps = [[*map(int, input().split())] for _ in range(n)]
    square = [i**2 for i in range(1, 127)]
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sum([(ps[i][k] - ps[j][k]) ** 2 for k in range(d)]) in square:
                cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()

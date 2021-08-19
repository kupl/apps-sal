def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        while n > 1:
            i = 0
            while i <= n * n:
                i += 1
                total = i * (i + 1) + i * (i - 1) // 2
                if total > n:
                    break
            i -= 1
            n -= i * (i + 1) + i * (i - 1) // 2
            i = 1
            cnt += 1
        print(cnt)
    return


def __starting_point():
    main()


__starting_point()

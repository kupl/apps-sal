def do(s, j):
    return int(s[:j]) + int(s[j:])


def main():
    n = int(input())
    x = input()
    mid = n // 2
    cnt = 0
    best = None
    for i in range(mid + 2):
        j = mid + i
        if j < n and x[j] != '0':
            val = do(x, j)
            cnt += 1
            if best is None:
                best = val
            else:
                best = min(best, val)

        j = mid - i
        if j > 0 and x[j] != '0':
            val = do(x, j)
            cnt += 1
            if best is None:
                best = val
            else:
                best = min(best, val)

        if cnt >= 7:
            break
    print(best)


def __starting_point():
    main()


__starting_point()

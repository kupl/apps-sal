USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, = list(map(int, input().split(' ')))
    p = [x - 1 for x in map(int, input().split(' '))]
    ans = [-1] * n
    for i in range(n):
        cnts = [0] * n
        j = i
        while True:
            cnts[j] += 1
            if cnts[j] == 2:
                ans[i] = j + 1
                break
            j = p[j]
    print(*ans)

    pass


def __starting_point():
    main()


__starting_point()

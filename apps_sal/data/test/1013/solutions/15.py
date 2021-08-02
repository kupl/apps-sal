def main():
    n, m = map(int, input().split())
    l = list(tuple(map(int, input().split())) for _ in range(n))
    lt = list(tuple(zip(*l)))
    print(4 - 2 * (any(l[0]) or any(l[-1]) or any(lt[0]) or any(lt[-1])))


def __starting_point():
    main()


__starting_point()

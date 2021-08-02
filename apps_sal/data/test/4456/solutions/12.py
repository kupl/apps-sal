def main():
    n, m = list(map(int, input().split()))
    abc = list('zyxwvutsrqponmlkjihgfedcba'[26 - m:])
    res = [abc[0]] * (n + 1)
    res[0], pool, f = 'YES\n', [False] * (n + 1), 0
    for p, q in zip(list(map(int, input().split())),
                    list(map(int, input().split()))):
        if pool[p]:
            f -= 1
        else:
            pool[p] = True
            f += 1
        if pool[q]:
            f -= 1
        else:
            pool[q] = True
            f += 1
        res[p] = abc[-1]
        if not f:
            del abc[-1]
            if not abc:
                break
    print('NO' if abc else ''.join(res))


def __starting_point():
    main()


__starting_point()

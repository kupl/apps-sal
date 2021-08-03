
def fixing(s, i, n, b):
    t, k = s[i], i + 1
    if not b and k < n and s[k] == s[i]:
        t = t * 2
        k += 1
    while k < n and s[k] == s[i]:
        k += 1

    return k, t, len(t) > 1


def main():
    s = list(input())
    i, n, b = 0, len(s), False
    w = ''
    while i < n:
        i, t, b = fixing(s, i, n, b)
        w += t
    print(''.join(w))


def __starting_point():
    main()


__starting_point()

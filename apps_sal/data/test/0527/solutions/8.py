def f():
    s, t = input(), input()
    n, m = len(s), len(t)
    table = [[]for i in range(26)]
    d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    for j in range(n):
        table[d[s[j]]].append(j)
    now = 0
    ind = 0
    if set(list(t)) - set(list(s)):
        print(-1)
        return
    from bisect import bisect_left as bl
    for p in t:
        if ind > table[d[p]][-1]:
            now += 1
            ind = 0
        ind = table[d[p]][bl(table[d[p]], ind)] + 1

    print(now * n + ind)


def __starting_point():
    f()


__starting_point()

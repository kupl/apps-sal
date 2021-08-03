n = int(input())
s = input()


def main(n, s):
    k = set()
    for i in range(n):
        k.add(s[i])
    v = len(k)
    h = dict()
    for i in k:
        h[i] = 0
    l = 0
    r = n
    while (l + 1 < r):
        m = (l + r) // 2
        f = False
        for i in h:
            h[i] = 0
        x = 0
        for i in range(m):
            h[s[i]] += 1
            if h[s[i]] == 1:
                x += 1
        if x == v:
            f = True
        else:
            for i in range(m, n):
                h[s[i - m]] -= 1
                if h[s[i - m]] == 0:
                    x -= 1
                h[s[i]] += 1
                if h[s[i]] == 1:
                    x += 1
                if x == v:
                    f = True
                    break
        if f:
            r = m
        else:
            l = m
    print(r)


main(n, s)

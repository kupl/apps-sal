def main():
    s = list(input())

    suffix = []
    for x in reversed(s):
        if suffix:
            suffix.append(min(suffix[-1], x))
        else:
            suffix.append(x)

    suffix = suffix[::-1]

    u = []
    t = []
    i = 0

    while True:
        m = suffix[i]

        while t and t[-1] <= m:
            u.append(t[-1])
            t.pop()

        while s[i] != m:
            t.append(s[i])
            i += 1

        u.append(s[i])

        i += 1
        if i == len(s):
            break

    u += t[::-1]

    print(''.join(u))


main()


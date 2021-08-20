def main():
    (n, k) = list(map(int, input().split()))
    (l, x) = (list(input()[::2]), k + 1)
    l.append('0')
    n += 1
    for (i, c) in enumerate(l):
        if c == '0':
            x -= 1
            if not x:
                break
    (m, j, ji) = (i, -1, (-1, i))
    for i in range(i + 1, n):
        if l[i] == '0':
            for j in range(j + 1, n):
                if l[j] == '0':
                    if m < i - j:
                        (m, ji) = (i - j, (j, i))
                    break
    (j, i) = ji
    j += 1
    z = i - j
    l[j:i] = ['1'] * z
    if z > n:
        z = n
    del l[-1]
    print(z)
    print(' '.join(l))


def __starting_point():
    main()


__starting_point()

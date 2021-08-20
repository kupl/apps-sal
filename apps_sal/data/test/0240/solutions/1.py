def main():
    s = input()
    if s in ('01', '10'):
        print(0)
        return
    cnt = [0] * 58
    for j in map(ord, s):
        cnt[j] += 1
    (n, s1) = (sum(cnt), input())
    for le in range(n - 1, 0, -1):
        if len(str(le)) + le == n:
            break
    for s in (s1, str(le)):
        for j in map(ord, s):
            cnt[j] -= 1
    res = [''.join([s1] + [chr(i) * a for (i, a) in enumerate(cnt) if a])] if s1[0] > '0' else []
    for i in range(49, 58):
        if cnt[i]:
            cnt[i] -= 1
            l = [chr(i) * a for (i, a) in enumerate(cnt) if a]
            l.append(s1)
            res.append(''.join([chr(i)] + sorted(l)))
            break
    print(min(res))


def __starting_point():
    main()


__starting_point()

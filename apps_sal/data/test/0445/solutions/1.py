def main():
    input()
    (l0, l1, ones) = ([], [], 0)
    for a in map(int, input().split()):
        if a == 1:
            ones += 1
        else:
            (l1 if a & 1 else l0).append(a)
    seive = [False, True] * (((max(l0) if l0 else 0) + (max(l1) if l1 else 0)) // 2 + 1)
    a = len(seive)
    for i in range(3, int(a ** 0.5) + 1, 2):
        if seive[i]:
            for j in range(i * i, a, i):
                seive[j] = False
    if ones:
        res = ['1'] * ones
        for a in l0:
            if a > 1 and seive[a + 1]:
                res.append(str(a))
                break
        if len(res) > 1:
            print(len(res))
            print(' '.join(res))
            return
    for a in l1:
        for b in l0:
            if seive[a + b]:
                print(2)
                print(a, b)
                return
    print(1)
    print(1 if ones else (l0 if l0 else l1)[0])


def __starting_point():
    main()


__starting_point()

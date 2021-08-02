def main():
    m, k = list(map(int, input().split()))
    all = set()
    zeros = ''
    for _ in range(k):
        zeros += '0'

    for _ in range(m):
        line = input().replace(' ', '')
        if line == zeros:
            print('YES')
            return
        all.add(line)

    for s1 in all:
        for s2 in all:
            if s1 == s2:
                continue
            bad = False
            for i in range(0, len(s1)):
                if s1[i] == '1' and s2[i] == '1':
                    bad = True
            if not bad:
                print('YES')
                return
    print('NO')


def __starting_point():
    main()


__starting_point()

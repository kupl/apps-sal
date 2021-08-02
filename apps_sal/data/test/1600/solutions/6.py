from collections import Counter


def __starting_point():
    n = int(input())
    data = list(map(int, input().split()))
    dd = {}
    for i, x in enumerate(sorted(data)):
        if x not in dd:
            dd[x] = i

    m = None
    c = 0
    n_pos = None

    counter = Counter()

    for i, x in enumerate(data):
        if n_pos is None:
            if dd[x] + counter[x] == i:
                c += 1
            else:
                n_pos = dd[x] + counter[x]
                m = x
        else:
            if x >= m:
                m = x
                n_pos = dd[x] + counter[x]

            if i == n_pos:
                c += 1
                n_pos = None

        counter[x] += 1

    print(c)


__starting_point()

def solve():
    _ = input()
    genom = list(input().strip())
    cntr = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '?': 0}
    for g in genom:
        cntr[g] += 1
    q = cntr['?']
    del cntr['?']
    maxval = max(cntr.values())
    needed = sum((maxval - val for val in list(cntr.values())))
    if needed > q:
        return '==='
    if (q - needed) % 4 != 0:
        return '==='
    maxval += (q - needed) // 4
    acgt = ('A', 'C', 'G', 'T')
    for i in range(len(genom)):
        if genom[i] == '?':
            for g in acgt:
                if cntr[g] < maxval:
                    genom[i] = g
                    cntr[g] += 1
                    break
    return ''.join(genom)


def __starting_point():
    print(solve())


__starting_point()

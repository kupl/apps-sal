def calc(n, m):
    import collections
    edict = dict()
    for i in range(1, len(m) + 2):
        edict[i] = []
    for j in range(len(m)):
        edict[m[j]].append(j)
    for k in edict:
        print((len(edict[k])))


def main():
    n = int(input())
    employees = list(int(v) for v in input().split())
    return calc(n, employees)


def __starting_point():
    main()


__starting_point()

def main():
    n = int(input())
    ar = []
    fi_values = map(int, input().strip().split())
    groups = dict()
    for (i, fi) in enumerate(fi_values):
        if fi not in groups:
            groups[fi] = []
        groups[fi].append(i + 1)
    g = [0] * n
    h = []
    for (k, v) in groups.items():
        if k not in v:
            print(-1)
            return
        else:
            h.append(k)
            for i in v:
                g[i - 1] = len(h)
    print(len(h))
    print(' '.join(map(str, g)))
    print(' '.join(map(str, h)))


main()

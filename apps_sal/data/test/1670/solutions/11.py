from collections import defaultdict


def main():
    ha = {'h': input().strip(), 'a': input().strip()}
    n = int(input().strip())
    d = defaultdict(list)
    for _ in range(n):
        t, a, player, card = input().strip().split()
        d[' '.join((ha[a], player))].append((int(t), {'y': 1, 'r': 2}[card]))
    res = []
    for k, l in d.items():
        l.sort()
        tot = 0
        for t, x in l:
            tot += x
            if tot > 1:
                res.append((t, k))
                break
    res.sort()
    for t, k in res:
        print(k, t)


main()

def main():
    n = int(input())
    ain = [input() for _ in range(2*n - 2)]
    a = sorted(ain, key=lambda x: len(x), reverse=True)

    s1 = a[0] + a[1][-1]
    d = { k: [] for k in a }

    next = False
    for i in range(1, n):
        try:
            d[s1[:i]].append('P')
            d[s1[-i:]].append('S')
        except KeyError:
            next = True

    if not next:
        result = []
        for e in ain:
            if not d[e]:
                break
            result.append(d[e][0])
            d[e].pop(0)
        else:
            print(''.join(result))
            return

    s1 = a[1] + a[0][-1]
    d = { k: [] for k in a }

    for i in range(1, n):
        d[s1[:i]].append('P')
        d[s1[-i:]].append('S')

    result = []
    for e in ain:
        if not d[e]:
            break
        result.append(d[e][0])
        d[e].pop(0)
    else:
        print(''.join(result))
        return

def __starting_point():
    main()

__starting_point()

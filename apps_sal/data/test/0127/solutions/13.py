

def main():
    n, f = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        k, m = [int(x) for x in input().split()]
        x = 0
        if k >= m:
            x = 0
        elif m < 2 * k:
            x = m - k
        else:
            x = k
        a.append([k, m, x])
    a.sort(key=lambda tup: tup[2], reverse=True)
    for i in range(f):
        a[i][0] += a[i][2]
    for i in range(n):
        a[i][2] = a[i][0] if a[i][0] < a[i][1] else a[i][1]
    print(sum(a[i][2] for i in range(n)))


def __starting_point():
    main()


__starting_point()

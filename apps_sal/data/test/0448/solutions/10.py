def main():
    n, m = input().split()
    n, m = int(n), int(m)
    a = []
    a = input().split()
    a = list(map(int, a))
    p = list(range(n))
    while len(a) > 1:
        if a[0] <= m:
            a = a[1:]
            p = p[1:]
        else:
            a[0] -= m
            a.append(a.pop(0))
            p.append(p.pop(0))

    print(p[0] + 1)


main()

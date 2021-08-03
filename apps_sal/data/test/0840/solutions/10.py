def main():
    n, k = list(map(int, input().split()))
    l = sorted(((a, b) for a, b in zip(list(map(int, input().split())), list(map(int, input().split())))),
               key=lambda e: (e[1] // e[0], e[1] - e[0] % e[1]))
    lo, hi = l[0][1] // l[0][0], (l[-1][1] + k) // l[-1][0] + 1
    l.append((0, 1))
    while lo < hi - 1:
        mid, x = (lo + hi) // 2, k
        for a, b in l:
            a *= mid
            if a > b:
                x -= a - b
                if x < 0:
                    hi = mid
                    break
            else:
                lo = mid
                break
    print(lo)


def __starting_point():
    main()


__starting_point()

def main():
    (n2, n3) = map(int, input().split())
    nmax = 3 * max(n2, n3) * 2
    c2 = c3 = c6 = 0
    for n in range(1, nmax):
        if n % 6 == 0:
            c6 += 1
        elif c3 < n3 and n % 3 == 0:
            c3 += 1
        elif c2 < n2 and n % 2 == 0:
            c2 += 1
        if n2 - c2 + n3 - c3 - c6 == 0:
            print(n)
            break


main()

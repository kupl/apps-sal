def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    def divisor(m):
        arr = [1, m]
        i = 2
        while i * i <= m:
            if m % i == 0:
                arr.append(i)
                if m // i != i:
                    arr.append(m // i)
            i += 1
        arr.sort()
        return arr
    (n, m) = map(int, input().split())
    a = divisor(m)
    for x in a:
        if x >= n:
            print(m // x)
            return


def __starting_point():
    main()


__starting_point()

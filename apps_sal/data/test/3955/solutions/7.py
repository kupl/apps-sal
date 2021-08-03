def solve(n, k, x, a):
    s = 0
    prefix = [0] * (n + 10)
    suffix = [0] * (n + 10)
    a.append(0)
    a.insert(0, 0)
    m = pow(x, k)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] | a[i]
    for i in range(n, 0, -1):
        suffix[i] = suffix[i + 1] | a[i]
    for i in range(1, n + 1):
        s = max(s, prefix[i - 1] | (a[i] * m) | suffix[i + 1])
    return s


def main(infile, outfile):
    n, k, x = list(map(int, infile.readline().split()))
    a = list(map(int, infile.readline().split()))
    outfile.write(str(solve(n, k, x, a)) + '\n')


def __starting_point():
    from sys import stdin, stdout
    main(stdin, stdout)


__starting_point()

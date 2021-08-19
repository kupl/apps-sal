# python3


def readline(): return tuple(map(int, input().split()))


def readlines(count): return (readline() for __ in range(count))


def main():
    n, = readline()
    z = dict(readlines(n))

    m, = readline()
    for (b, y) in readlines(m):
        z[b] = max(z.setdefault(b, y), y)

    print(sum(z.values()))


main()

from functools import reduce


def main():
    from sys import stdin, stdout
    from functools import reduce
    from operator import xor

    n = int(int(input()))
    mat = [list(map(int, input().split())) for _ in range(n)]
    ans, q, a = reduce(xor, [mat[i][i] for i in range(n)]), int(input()), []
    queries = [stdin.readline() for i in range(q)]

    for query in queries:
        if query[0] == '3':
            a.append(str(ans))
        else:
            ans ^= 1
    print(''.join(a))


def __starting_point():
    main()


__starting_point()

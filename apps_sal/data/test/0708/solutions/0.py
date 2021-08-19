def main():
    (n, k) = (int(x) for x in input().split())
    (a, b, c, d) = (int(x) for x in input().split())
    (path1, path2) = solver(n, k, a, b, c, d)
    if path1 == None:
        print(-1)
    else:
        for x in path1:
            print(x, end=' ')
        print()
        for x in path2:
            print(x, end=' ')


def solver(n, k, a, b, c, d):
    if k <= n or n == 4:
        return (None, None)
    else:
        path1 = [a, c] + [i for i in range(1, n + 1) if i not in (a, b, c, d)] + [d, b]
        path2 = [c, a] + [i for i in range(1, n + 1) if i not in (a, b, c, d)] + [b, d]
        return (path1, path2)


main()

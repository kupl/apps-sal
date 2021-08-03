def main():
    n = int(input())
    a = [int(x) - 1 for x in input().split()]

    for i, s1 in enumerate(a):
        visited = {i}

        next = s1
        while next not in visited:
            visited.add(next)
            next = a[next]

        print(next + 1, end=' ')


def __starting_point():
    main()


__starting_point()

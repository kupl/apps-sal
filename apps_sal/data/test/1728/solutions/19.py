
def main():
    n = int(input())
    parents = [int(x) - 1 for x in input().strip().split()]
    colors = [int(x) for x in input().strip().split()]

    ans = 1

    for i in range(n - 1):
        c = i + 1
        p = parents[i]
        if (colors[c] != colors[p]):
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()

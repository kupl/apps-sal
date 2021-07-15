def main():
    n = int(input())
    ans = set()
    for _ in range(n):
        a = int(input())
        if a in ans:
            ans.discard(a)
        else:
            ans.add(a)

    print((len(ans)))


def __starting_point():
    main()

__starting_point()

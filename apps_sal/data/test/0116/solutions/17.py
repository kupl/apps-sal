def solve():
    l1, r1, l2, r2, k = list(map(int, input().split(' ')))

    start = max(l1, l2)
    end = min(r1, r2)

    ans = max(0, end - start + 1)

    if start <= k <= end:
        ans -= 1

    print(ans)


def main():
    solve()

def __starting_point():
    main()

__starting_point()

def main():
    import sys
    input = sys.stdin.readline

    def solve():
        a, b, c, d, k = list(map(int, input().split()))
        x = (a + c - 1) // c
        y = (b + d - 1) // d
        if x + y > k:
            print(-1)
        else:
            print(x, y)

    for _ in range(int(input())):
        solve()

    return 0


main()

def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        ans += b - a + 1
    print(ans)


def __starting_point():
    main()

__starting_point()

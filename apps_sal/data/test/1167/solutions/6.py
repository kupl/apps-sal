def solve():
    a, b, c, d, k = list(map(int, input().split()))
    x = (a + c - 1) // c
    y = (b + d - 1) // d
    if x + y > k:
        print(-1)
    else:
        print(x, y)


def main():
    t = int(input())
    for _ in range(t):
        solve()


main()

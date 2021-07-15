def main():
    n, m = list(map(int, input().split()))
    ans = ["x" for _ in range(n)]
    if n == 1 and m == 0:
        print((0))
        return

    for _ in range(m):
        s, c = list(map(int, input().split()))
        if (s == 1 and c == 0 and n != 1) or s > n:
            print((-1))
            return

        if ans[s-1] != "x" and ans[s-1] != str(c):
            print((-1))
            return

        ans[s-1] = str(c)

    if ans[0] == "x":
        ans[0] = "1"
    print(("".join(ans).replace("x", "0")))


def __starting_point():
    main()

__starting_point()

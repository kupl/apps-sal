def solve():
    n = int(input())
    arr = [int(k) for k in input().split()]
    arr.sort()
    if n == 2:
        print(0)
        return
    ans = arr[-1] - arr[1]
    ans = min(ans, arr[-2] - arr[0])
    print(ans)


def __starting_point():
    solve()


__starting_point()

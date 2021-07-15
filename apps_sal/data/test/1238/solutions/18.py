def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    mn, mx = min(a), max(a)
    print(mx - mn + 1 - n)

__starting_point()

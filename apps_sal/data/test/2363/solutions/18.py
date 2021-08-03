def solve():
    a, b = list(map(int, input().rstrip().split()))
    count = 0
    if b > a:
        a, b = b, a
    while not (a == 0 or b == 0):
        count += a // b
        a %= b
        a, b = b, a
    print(count)


def __starting_point():
    t = int(input())
    for _ in range(t):
        solve()


__starting_point()

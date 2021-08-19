def main():
    import sys
    input = sys.stdin.readline

    def intersection(a, b, c, d):
        return (max(a, c), min(b, d))

    def solve():
        (n, k) = map(int, input().split())
        arr = list(map(int, input().split()))
        (a, b) = (0, 10 ** 18)
        for x in arr:
            (a, b) = intersection(a, b, x - k, x + k)
        if a > b:
            print(-1)
        else:
            print(b)
    for _ in range(int(input())):
        solve()
    return 0


main()

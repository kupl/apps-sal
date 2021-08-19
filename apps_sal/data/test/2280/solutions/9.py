def main():

    def solve():
        n = int(input())
        arr = sorted(map(int, input().split()))
        a = arr[-2]
        print(min(n - 2, a - 1))
    import sys
    input = sys.stdin.readline
    for _ in range(int(input())):
        solve()
    return 0


main()

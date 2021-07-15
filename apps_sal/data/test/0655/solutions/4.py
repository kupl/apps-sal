def solve(x, y, n):
    return "White" if (x-1 + y-1) <= (n-x + n-y) else "Black"


def main():
    n = int(input())
    x, y = [int(i) for i in input().split()]
    print(solve(x, y, n))


main()


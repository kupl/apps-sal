import itertools


def solve(n):
    ans = (n + 1) // 2
    return ans - 1


def main():
    n = int(input())
    print(solve(n))


main()

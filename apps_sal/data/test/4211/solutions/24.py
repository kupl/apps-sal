import sys
input = sys.stdin.readline


def main():
    numbers = []
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = numbers[0]
    dp[-1] = numbers[-1]
    for i in range(1, n - 1):
        dp[i] = min(numbers[i - 1], numbers[i])
    print(sum(dp))


def __starting_point():
    main()


__starting_point()

import copy
import sys
input = sys.stdin.readline


def main():
    questions = []
    dp = []
    n = int(input())
    questions = list(map(int, input().split()))
    m = int(input())
    drinks = [list(map(int, input().split())) for _ in range(m)]
    for drink in drinks:
        dp = copy.deepcopy(questions)
        dp[drink[0] - 1] = drink[1]
        print(sum(dp))


def __starting_point():
    main()


__starting_point()

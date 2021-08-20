from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    power = [1]
    for i in range(N):
        power.append(power[-1] * 2 % MOD)
    ans = 0
    for (i, c) in enumerate(C):
        ans += c * (power[N - 2] * power[N] * (N - i - 1)) % MOD
        ans += c * (power[N - 1] * power[N]) % MOD
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()

import sys
input = sys.stdin.readline
mod = 1000000007


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(MI())


(N, K) = MI()
MAX = sum(range(N - K + 2, N + 1))
MIN = sum(range(0, K - 1))
ans = 0
for k in range(K, N + 2):
    MAX += N - k + 1
    MIN += k - 1
    ans += (MAX - MIN + 1) % mod
print(ans % mod)

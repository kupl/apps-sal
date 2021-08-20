import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def divisors(n):
    lower = []
    upper = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
    lower.extend(reversed(upper))
    return lower


def main():
    (N, M) = list(map(int, readline().split()))
    divisor = divisors(M)
    for d in reversed(divisor):
        if M // d >= N:
            ans = d
            break
    print(ans)
    return


def __starting_point():
    main()


__starting_point()

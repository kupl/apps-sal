import sys
import math
input = sys.stdin.readline


def main():
    (N, X) = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    ans = abs(x[0] - X)
    for i in range(N):
        ans = math.gcd(ans, abs(x[i] - x[i + 1]))
    print(ans)


def __starting_point():
    main()


__starting_point()

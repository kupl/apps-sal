import sys
import math
pin = sys.stdin.readline


def main():
    N = int(pin())
    ans = int(pin())
    for i in range(N - 1):
        T = int(pin())
        ans = (ans * T) // math.gcd(ans, T)
    print(ans)
    return


main()

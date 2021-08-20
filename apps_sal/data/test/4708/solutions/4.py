import math
from datetime import date


def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    ans = max(0, n - k) * y + min(n, k) * x
    print(ans)


main()

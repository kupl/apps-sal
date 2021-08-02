import math
import numpy as np
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i // math.gcd(ans, i)
    print(ans + 1)


main()

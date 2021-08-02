from math import gcd
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, k = list(map(int, input().split()))
    S = input().strip()

    LIST = [0] * 26
    for s in S:
        LIST[ord(s) - 97] += 1

    for x in range(n, 0, -1):
        GCD = gcd(x, k)
        p = x // GCD

        SUM = 0
        for l in LIST:
            if l >= p:
                SUM += l // p * p

        if SUM >= x:
            print(x)
            break

    # print(S)

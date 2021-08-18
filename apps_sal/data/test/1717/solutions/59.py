from math import ceil, floor, sqrt, gcd, log
import sys
input = sys.stdin.readline
def ri(): return int(input())
def rl(): return list(map(int, input().split()))
def rs(): return input()


for _ in range(1):
    N = ri()
    ans = 1
    for i in range(2, N + 1):
        ans = ans * i // gcd(ans, i)
    print(ans + 1)

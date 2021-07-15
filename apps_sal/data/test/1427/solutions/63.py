import math
import sys


def lcm(a, b):
  return a * b // math.gcd(a, b)


input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
LCM = 1
ans = 0
MOD = 1000000007
for x in A:
  LCM = lcm(LCM, x)
for x in A:
  ans += LCM // x

print(ans%MOD)

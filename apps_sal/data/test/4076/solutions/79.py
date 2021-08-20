import sys
import math
from decimal import Decimal


def input():
    return sys.stdin.readline().rstrip()


(A, B, H, M) = map(float, input().split())
minute = H * 60 + M
short = minute / (60 * 12) * 2 * math.pi
long = M / 60 * 2 * math.pi
rad = abs(long - short)
ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad))
print(ans)

import math
import collections
def ii(): return int(input())


def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


a, b = mi()
print((a * b) // math.gcd(a, b))

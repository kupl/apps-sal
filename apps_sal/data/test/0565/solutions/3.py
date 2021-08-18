
import sys
input = sys.stdin.readline
def mii(): return list(map(int, input().split()))


a, b, c = mii()
b -= 1
c -= 2
print(min(a, b, c) * 3 + 3)

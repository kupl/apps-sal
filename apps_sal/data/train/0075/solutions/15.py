import sys
from math import pi, sin
def I():
    return sys.stdin.readline().rstrip()

def h(n):
    m = n // 2 - 0.5
    a = 1
    return a * sin(pi * m / n) / sin(pi / n)

def main():
    for tc in range(1, 1+int(I())):
        n = int(I())
        n *= 2
        print(h(n))

main()


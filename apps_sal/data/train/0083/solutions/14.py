import sys
import math

def input():
    return sys.stdin.readline().strip()

def iinput():
    return [int(x) for x in sys.stdin.readline().split()]

def main():
    x, y, a, b = iinput()
    if (y - x) % (a + b) == 0:
        print((y - x) // (a + b))
    else:
        print(-1)
    return

for ______ in range(int(input())):
    main()


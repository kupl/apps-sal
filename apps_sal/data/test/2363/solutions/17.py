import math, sys

def solve(a, b):
    if a == b:
        return 1
    elif a == 0 or b == 0:
        return 0
    else:
        return math.floor(max(a,b)/min(a,b)) + solve(min(a,b), max(a,b) % min(a,b))

def main():
    n = int(input())
    for s in sys.stdin:
        a, b = [int(x) for x in s.split()]
        print(solve(a,b))

def __starting_point():
    main()

__starting_point()

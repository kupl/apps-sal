import sys

sys.setrecursionlimit(10 ** 6)
def MI(): return map(int, sys.stdin.readline().split())


def main():
    x, y = MI()
    if x > y: x, y = y, x
    if y > x + 1: print("Alice")
    else: print("Brown")


main()

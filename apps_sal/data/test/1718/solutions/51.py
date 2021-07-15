import sys
import math
def input(): return sys.stdin.readline().strip()

sys.setrecursionlimit(250000)

def main():
    n,k = map(int, input().split())
    a = list(map(int,input().split()))

    sum_ = n
    count = 0
    while sum_ > 0:
        if sum_ > k:
            sum_ = sum_ - k + 1
            count += 1
        else:
            sum_ = 0
            count += 1
    print(count)
def __starting_point():
    main()
__starting_point()

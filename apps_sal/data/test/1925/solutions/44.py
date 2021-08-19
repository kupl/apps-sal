import math
import sys
input = sys.stdin.readline


def main():
    (A, B, N) = map(int, input().split())
    x = min(B - 1, N)
    print(math.floor(A * x / B) - A * math.floor(x / B))


main()

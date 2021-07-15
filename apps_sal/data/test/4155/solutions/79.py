import sys
import math
sys.setrecursionlimit(500000)
INF = float('inf')

def solve(h, water):
    left = 0
    while left < len(h) - 1 and h[left] == 0:
        left += 1
    right = left
    while right < len(h) and h[right] != 0:
        right += 1

    if left < right:
        h[left:right] = [i - 1 for i in h[left:right]]
    elif left == right and h[left] > 0:
        h[left] = h[left] - 1
    else:
        return water
        
    water = solve(h, water + 1)
    return water

def main():
    n = int(input())
    h = list(map(int, input().split()))
    return solve(h, 0)

def __starting_point():
    print((main()))

__starting_point()

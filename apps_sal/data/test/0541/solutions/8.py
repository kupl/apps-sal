import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N, M = NMI()
    ab = [NLI() for _ in range(M)]
    
    ENDsorted_sections= sorted(ab, key=lambda x: x[1])
    
    ans = 1
    dropped_bridge = ENDsorted_sections[0][1]

    for m in range(M):
        if ENDsorted_sections[m][0] >= dropped_bridge:#新しく橋を落とさないといけない
            ans += 1
            dropped_bridge = ENDsorted_sections[m][1]
    print(ans)    

def __starting_point():
    main()
__starting_point()

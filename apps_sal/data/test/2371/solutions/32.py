import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def main():
    n,z,w = map(int,input().split())
    a = list(map(int,input().split()))
    if n == 1:
        ans = abs(w - a[0])
    else:
        ans = max(abs(w - a[-1]),abs(a[-1] - a[-2]))
    print(ans)

def __starting_point():
    main()
__starting_point()

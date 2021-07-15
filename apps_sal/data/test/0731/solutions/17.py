import sys

def solve():
    w,m,k, = rv()
    small, large = 0, int(1e16)
    while small < large:
        avg = (small + large + 1) // 2
        if works(avg, w, m, k): small = avg
        else: large = avg - 1
    print(small)

def works(numbers, maxcost, startnum, multiplier):
    maxnumber = numbers + startnum - 1
    res = 0
    for length in range(1, 20):
        goodoflength = max(0, maxnumber - (pow(10, length - 1) - 1))
        badoflength = max(0, startnum - (pow(10, length - 1) - 1) - 1)
        res += (goodoflength - badoflength)
    return res * multiplier <= maxcost

def rv(): return list(map(int, input().split()))
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()




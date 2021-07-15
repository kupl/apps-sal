from heapq import heappop, heappush
import sys

def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))

def Main():
    n, m = read_ints()
    query = [[] for _ in range(m)]
    for _ in range(n):
        a, b = read_ints()
        if m - a < 0: continue
        query[m - a].append(b)

    total = 0
    que = []
    for i, b in enumerate(query):
        for x in b:
            heappush(que, x)
            total += x
        while len(que) > i + 1:
            x = heappop(que)
            total -= x
    print(total)

def __starting_point():
    Main()

__starting_point()

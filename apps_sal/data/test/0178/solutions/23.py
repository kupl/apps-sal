import sys
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(int(1e7))


def main():
    n = int(input().strip())
    s = input().strip()
    V = [i for i in range(n) if s[i] != '8']
    P = [i for i in range(n) if s[i] == '8']
    heapify(V)
    heapify(P)
    while len(V) + len(P) > 11 and len(V) * len(P) > 0:
        heappop(V)
        heappop(P)
    yes = len(V) == 0 or (len(V) * len(P) > 0 and P[0] < V[0])
    print('YES' if yes else 'NO')
    return


while 1:
    try:
        main()
    except EOFError:
        break

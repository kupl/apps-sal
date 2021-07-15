import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7

def read_values(): return list(map(int, input().split()))
def read_index(): return [int(x) - 1 for x in input().split()]
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n) 


def main():
    N = int(input())
    S = read_list()

    res = V(max, 0)
    for c in range(1, N):
        r = 0
        t1 = 0
        t2 = N - 1
        a = t2 - c
        while True:
            if a < c:
                break
            
            if (N - 1) % c == 0 and 2 * a <= N - 1:
                break

            t1 += c
            t2 -= c
            a -= c
            r += S[t1] + S[t2]
            res.ud(r)

    print(res)


def __starting_point():
    main()

__starting_point()

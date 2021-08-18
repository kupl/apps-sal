import sys
from collections import Counter, deque, defaultdict

MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def Main():
    n, q = read_ints()
    tree = [[] for _ in range(n)]
    c = [0] * n
    for _ in range(n - 1):
        a, b = read_ints()
        tree[~-a].append(~-b)
        tree[~-b].append(~-a)
    for _ in range(q):
        p, x = read_ints()
        c[~-p] += x
    que = deque([0])
    seen = [False] * n
    while que:
        p = que.pop()
        seen[p] = True
        for x in tree[p]:
            if seen[x]:
                continue
            que.append(x)
            c[x] += c[p]

    print(*c)


def __starting_point():
    Main()


__starting_point()

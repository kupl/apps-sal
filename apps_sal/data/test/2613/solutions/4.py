import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    n, k, z = MI()
    aa = LI()
    r = max(0, k - 2 * z)
    s = sum(aa[:r + 1])
    ans = -1
    for i in range(min(n - 1, k)):
        if i + 1 <= r: cur = s + (aa[i] + aa[i + 1]) * z
        else:
            s += aa[i + 1]
            left = k - i - 1
            cur = s + aa[i + 1] * (left // 2) + aa[i] * (left - left // 2)
        ans = max(ans, cur)
    print(ans)

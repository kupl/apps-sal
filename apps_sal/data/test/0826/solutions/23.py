import sys
sys.setrecursionlimit(10 ** 6)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LC(): return list(input())
def IC(): return [int(c) for c in input()]
def LLI(rows_number): return [LI() for _ in range(rows_number)]


N = II()
if(N == 1):
    print(1)
else:
    Big = N + 1
    NG = 0
    OK = Big

    def is_ok(arg):
        return ((arg + 2) * (arg + 3)) // 2 >= Big

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    l = meguru_bisect(NG, OK)
    while(l * (l + 1) // 2 <= Big):
        l += 1
    l -= 1
    print(Big - l)

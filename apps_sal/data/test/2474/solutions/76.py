MOD = 10**9+7

def solve(C):
    N = len(C)
    C.sort()

    dp1 = 0
    dp2 = 0
    for k,c in enumerate(C):
        ndp2 = 2*pow(4,k,MOD)*c + 4*dp2
        dp1 = 4*dp1 + ndp2 - 2*dp2
        dp2 = ndp2
        dp1 %= MOD
        dp2 %= MOD

    return dp1

def naive(C):
    from itertools import product
    N = len(C)
    C.sort()
    s = 0
    for a in product(range(2),repeat=N):
        for b in product(range(2),repeat=N):
            pop = 1
            for x,y,c in zip(a,b,reversed(C)):
                if x != y:
                    s += c*pop
                    pop += 1
    return s

def __starting_point():
    N = int(input())
    C = list(map(int,input().split()))
    print(solve(C))
__starting_point()

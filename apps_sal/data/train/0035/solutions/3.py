import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    Ans = [0] * T
    for t in range(T):
        N = int(input())
        A = [int(a) for a in input().split()]
        skillDict = dict()
        for a in A:
            if a in skillDict: skillDict[a] += 1
            else: skillDict[a] = 1
        for i in range(1, N+1):
            if i in skillDict:
                Ans[t] += skillDict[i] // i
                if i+1 not in skillDict: skillDict[i+1] = 0
                skillDict[i+1] += skillDict[i] % i
    print("\n".join(map(str, Ans)))
  

    return 0

def __starting_point():
    solve()
__starting_point()

import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    N, P = map(int, input().split())
    S = input().strip("\n")
    modSum = 0
    modDict = defaultdict(int)
    modDict[0] += 1
    ans = 0

    if P == 2 or P == 5:
        for i in range(N):
            if int(S[i]) % P == 0:
                ans += i + 1
        
    else:
        for i in range(N):
            modSum += int(S[N-i-1]) * pow(10, i, P)
            modSum %= P
            modDict[modSum] += 1

        for key in modDict:
            v = modDict[key]
            ans += v * (v - 1) // 2
    
    print(ans)

    return 0

def __starting_point():
    solve()
__starting_point()

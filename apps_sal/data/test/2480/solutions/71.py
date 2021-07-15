import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [(int(a) % K) - 1 for a in input().split()]
    sum_A = [0 for _ in range(N + 1)]

    count = 0
    modK = dict()
    modK[0] = [0]
    for i in range(N):
        sum_A[i + 1] = (sum_A[i] + A[i]) % K
        if sum_A[i+1] not in modK: modK[sum_A[i+1]] = [i + 1]
        else: modK[sum_A[i+1]].append(i+1)
    
    for key in modK: 
        lenK = len(modK[key])
        for i, a in enumerate(modK[key]):
            count += bisect_left(modK[key], a + K, i, lenK) - i - 1

    print(count)
    return 0

def __starting_point():
    solve()
__starting_point()

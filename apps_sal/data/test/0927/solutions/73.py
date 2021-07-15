import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

from copy import deepcopy
def compare(A,B):
    tot_a = sum(A)
    tot_b = sum(B)
    if tot_a > tot_b:
        return A
    if tot_b > tot_a:
        return B
    for i in range(9,0,-1):
        if A[i] > B[i]:
            return A
        elif A[i] < B[i]:
            return B

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    match = (-1,2,5,5,4,5,6,3,7,6)

    dp = [[0]*10 for _ in range(1 + N)]
    changed = [0] * (N + 1)
    changed[0] = 1
    for i in range(N):
        for j in A:
            if i + 1 - match[j] >= 0 and changed[i + 1 - match[j]]:
                B = deepcopy(dp[i + 1 - match[j]])
                B[j] += 1
                if compare(dp[i + 1],B) == B:
                    dp[i + 1] = B
                    changed[i + 1] = 1
    ans = ''
    for i in range(9,0,-1):
        ans += str(i) * dp[-1][i] 
    print(ans)    
def __starting_point():
    main()
__starting_point()

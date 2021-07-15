import sys, math
input = sys.stdin.readline

def getInts():
    return [int(s) for s in input().split()]

def getInt():
    return int(input())

def getStrs():
    return [s for s in input().split()]

def getStr():
    return input().strip()

def listStr():
    return list(input().strip())

import collections as col
import math

def solve():
    N, M, K = getInts()
    P = getInts()
    #suppose we have already chosen i blocks of m, and the last used index was j
    #deal with worst case in order N log N time
    if M == 1:
        P.sort(reverse=True)
        return sum(P[:K])
    PP = [0]
    curr_sum = 0
    for p in P:
        curr_sum += p
        PP.append(curr_sum)
    dp = [[0 for j in range(N+1)] for i in range(K+1)]
    #dp[0][j] = 0 for all j
    #dp[i][0] = 0 for all i
    #Consider dp[1][0] (suppose M==1)
    #dp[1][1] = min(dp[0][1],dp[0][0]+PP[1]-PP[0])
    
    for i in range(1,K+1):
        #j is the number of elements used, i.e. up to index j-1 since it is 0-based
        for j in range(1,N+1):
            if i*M > j:
                continue
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-M]+PP[j]-PP[j-M])
    #print(dp)
    return dp[K][N]
    
print(solve())
    



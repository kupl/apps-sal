import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    A = NLI()
    B = NLI()
    C = NLI()
    
    A = sorted(A)
    C = sorted(C)
    
    ans = 0
    
    for b in B:
        

        A_ng = -1       #ng:とり得る最小の値-1
        A_ok = len(A)  #ok:とり得る最大の値+1

        while (abs(A_ok - A_ng) > 1):
            A_mid = (A_ok + A_ng) // 2

            if A[A_mid] >= b:#計算の結果、midが条件を満たすならokにmidを代入。そうでなければngにmidを代入。
                A_ok = A_mid
            else:
                A_ng = A_mid
                
        C_ng = -1      #ng:とり得る最小の値-1
        C_ok = len(C)  #ok:とり得る最大の値+1

        while (abs(C_ok - C_ng) > 1):
            C_mid = (C_ok + C_ng) // 2

            if C[C_mid] > b:#計算の結果、midが条件を満たすならokにmidを代入。そうでなければngにmidを代入。
                C_ok = C_mid
            else:
                C_ng = C_mid
                
                
        len_C = len(C)
        
        ans += A_ok * (len_C-C_ok)
        
    print(ans)
def __starting_point():
    main()
__starting_point()

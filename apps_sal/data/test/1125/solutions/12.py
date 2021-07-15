import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]
def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    ref=0
    for i in range(2,N):
        ref^=A[i]
    
    a0=A[0]
    a1=A[1]
    ans=0
    #print(bin(a0),bin(a1),bin(ref))
    INF=10**13
    @lru_cache(None)
    def dfs(a0,a1,ref):
        inf=INF
        if (a0 & 1) ^ (a1 & 1) != (ref & 1):
            return inf
        
        if a0<0:
            return inf
        if ref == 0:
            return inf if a0<a1 else (a0-a1)//2
        a01=a0&1
        a11=a1&1
        ref1=ref&1
        ans=inf
        if a01^a11==ref1:
            ans=min(ans,2*dfs(a0>>1,a1>>1,ref>>1))
        ans=min(ans,2*dfs((a0-1)//2,(a1+1)//2,ref>>1)+1)

        return ans
    x=dfs(a0,a1,ref)
    if x>=a0:
        print(-1)
    else:
        print(x)
    # for j in range(0,41):
    #     a0j=(a0>>j)&1
    #     a1j=(a1>>j)&1
        
    #     refj=(ref>>j)&1
    #     #print(a0j,a1j,refj)
    #     if a0j^a1j==refj:
    #         nref=(ref>>(j+1))&1

    #         na0=((a0>>(j+1))&1)
    #         na1=((a1>>(j+1))&1)
            
    #         if ((a0>>(j+1))&1)^((a1>>(j+1))&1)!=nref:
    #             #print("a",na0,na1,nref)
    #             shif=1<<j
    #             if a0>0 and (((a0-shif))^(((a1+shif))==ref:
    #                 ans+=shif
    #                 a0-=shif
    #                 a1+=shif


    #         continue
    #     else:
    #         shif=1<<j

    #         ans+=shif
    #         a0-=shif
    #         a1+=shif
    #         #print(shif,a0,a1)
    #         if a0<0:
    #             print(-1)
    #             return









def __starting_point():
    main()
__starting_point()

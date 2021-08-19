import sys
input = sys.stdin.readline

#l = list(map(int, input().split()))
#import numpy as np
#arr = np.array([int(i) for i in input().split()])
'''
a,b=[],[]
for i in range(n):
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''


def premf(n):
    # 前処理
    # minfactor:複数の素因数分解を高速(O(Q*logA_max))に行う,indexはその整数
    # return resで素数リスト(eratosthenes),MinFactorで前処理用リスト返す
    IsPrime = [False] + [False] + [True] * (n - 1)

    res = []
    for j in range(4, n + 1, 2):
        IsPrime[j] = False
    for i in range(1, n + 1, 2):
        if IsPrime[i]:
            for j in range(i * 2, n + 1, i):
                IsPrime[j] = False

            if IsPrime[(i + 1) // 2]:
                res.append(i)

    return res


q = int(input())
n = 10**5
res = premf(n)
a = [0] * (10**5 + 1)  # 1-index
t = 0
# print(res)
for i in range(len(res)):
    t += 1
    a[res[i]] = t
for i in range(10**5):
    if a[i + 1] == 0:
        a[i + 1] = a[i]
# print(a[:20])
for i in range(q):
    l, r = map(int, input().split())
    print(a[r] - a[l - 1])

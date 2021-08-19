"""
Created on Fri Sep 18 00:26:07 2020

@author: liang
"""
import math
'\nコーナーケース１:\n    重複があるとき\u3000not coprime(※これが誤り)\n    ただし、1の重複は除く\n\nコーナーケース:\n    重複があるとき\u3000pairwise coprime ではない\n    setwise coprimeの可能性はある\n    ただし、１の重複は\n'
C = 10 ** 6
N = int(input())
judge = [0] + [False] * C
A = list()
f = True
for a in input().split():
    if judge[int(a)] == True and int(a) != 1:
        f = False
    judge[int(a)] = True
    A.append(int(a))
d = [False] + [True] * C


def solve(f):
    flag = True
    for i in range(2, C + 1):
        count = 0
        if d[i] == True:
            for j in range(i, C + 1, i):
                if judge[j] == True:
                    count += 1
                if count == 2:
                    flag = False
                    break
                d[j] = False
        if not flag:
            break
    if flag == True and f == True:
        return 'pairwise coprime'
    ans = A[0]
    for i in range(N):
        ans = math.gcd(ans, A[i])
    if ans == 1:
        return 'setwise coprime'
    return 'not coprime'


print(solve(f))

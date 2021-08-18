from collections import Counter
import sys
input = sys.stdin.readline

#l = list(map(int, input().split()))
#import numpy as np
#arr = np.array([int(i) for i in input().split()])
'''
a,b=[],[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

n = int(input())


def soinsuu(n):
    # 素因数分解リスト生成,collections.Counter(a)で個数取得
    # 1に対しては[]をreturn
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


a = Counter(soinsuu(n))
if n == 1:
    print(0)
    return
# print(a)
cnt = 0
for i in range(1, 1 + max(a.values())):
    for item in a.keys():
        # print(i,item)
        if n % (item**i) == 0:
            n //= item**i
            # print(n,item)
            cnt += 1
            if n == 1:
                break

print(cnt)

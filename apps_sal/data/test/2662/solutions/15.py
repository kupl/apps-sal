import bisect
# from collections import deque
# from collections import Counter
# from fractions import gcd # >=Python3.5 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # <Python3.5
# from math import sqrt

n = int(input())
li = [int(input()) for i in range(n)]
li = [-x for x in li]

X = []
X.append(li[0])

for i in range(1, n):
    idx = bisect.bisect_right(X, li[i])
    if idx == len(X):
        X.append(li[i])
    else:
        X[idx] = li[i]

print(len(X))

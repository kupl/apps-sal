from math import *


class slopeC:
    def __init__(self):
        self.chil = set()


n = int(input())

slopes = {}
L = []
for i in range(n):
    x, y = list(map(int, input().split()))

    for l in L:
        if x != l[0]:
            slope = (y - l[1]) / (x - l[0])
        else:
            slope = inf

        s1 = str(l[0]) + '-' + str(l[1])
        s2 = str(x) + '-' + str(y)
        if slope not in slopes:
            slopes[slope] = [slopeC()]
            slopes[slope][0].chil.add(s1)
            slopes[slope][0].chil.add(s2)
        else:
            f = 0
            for child in slopes[slope]:
                if s1 in child.chil:
                    f = 1
                    child.chil.add(s2)
                    break
            if f == 0:
                slopes[slope] += [slopeC()]
                slopes[slope][0].chil.add(s1)
                slopes[slope][0].chil.add(s2)

    L += [[x, y]]
A = []
P = [0]
for s in slopes:
    A += [(len(slopes[s]))]
    P += [P[-1] + A[-1]]

ans = 0


for i, v in enumerate(A):
    ans += A[i] * (P[-1] - P[i + 1])
print(ans)

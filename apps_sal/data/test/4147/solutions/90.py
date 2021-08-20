import copy
from itertools import combinations
import sys
input = sys.stdin.readline
(N, A, B, C) = (int(i) for i in input().split())
l = [0] * N
for i in range(N):
    l[i] = int(input())
mp = []
for na in range(1, N - 1):
    for ja in combinations(l, na):
        l_b = copy.copy(l)
        for i2 in ja:
            if i2 in l_b:
                l_b.remove(i2)
        for nb in range(1, N):
            for jb in combinations(l_b, nb):
                l_c = copy.copy(l_b)
                for i3 in jb:
                    if i3 in l_c:
                        l_c.remove(i3)
                for nc in range(1, N + 1):
                    for jc in combinations(l_c, nc):
                        AA = abs(A - sum(ja)) + 10 * (na - 1)
                        BB = abs(B - sum(jb)) + 10 * (nb - 1)
                        CC = abs(C - sum(jc)) + 10 * (nc - 1)
                        mp.append(AA + BB + CC)
print(min(mp))

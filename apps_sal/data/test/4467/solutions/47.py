import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li2(N)
B = li2(N)

A = sorted(A, key=lambda x:x[1])
B = sorted(B, key=lambda x:x[0])

flag = [0] * N

for i in range(N):
    ind = -1
    for j in range(N):
        if A[j][1] < B[i][1]:
            ind = j
    while ind >= 0:
        if not flag[ind] and A[ind][0] < B[i][0]:
            flag[ind] = 1
            break
        ind -= 1

#print(flag)
print(sum(flag))

import sys
input = sys.stdin.readline
import itertools
import numpy as np
from scipy.sparse.csgraph import connected_components

H,W = map(int,input().split())
words = np.array([list(input().rstrip()) for _ in range(H)], dtype='U1')

def gen_pair_pattern_even(rest):
    # 偶数個を仮定
    if len(rest) == 0:
        yield []
        return
    if len(rest) == 1:
        x = rest.pop()
        yield [(x,x)]
        return
    li = list(rest)
    x = li[0]
    for y in li[1:]:
        se = rest.copy()
        se.remove(x)
        se.remove(y)
        for p in gen_pair_pattern_even(se):
            yield p + [(x,y)]    

def gen_pair_pattern(N):
    if N & 1:
        for n in range(N):
            se = set(x for x in range(N) if x != n)
            for p in gen_pair_pattern_even(se):
                yield p + [(n,n)]
    else:
        for p in gen_pair_pattern_even(set(range(N))):
            yield p

def test(row_pairs):
    graph = np.ones((W,W), dtype = np.bool)
    for r1,r2 in row_pairs:
        graph &= (words[r1][:,None] == words[r2][None,:])
    graph &= graph.T
    se = set(range(W))
    while se:
        removed = False
        for i,j in itertools.combinations(se,2):
            if graph[i,j]:
                se.remove(i)
                se.remove(j)
                removed = True
                break
        if not removed:
            break
    if len(se) > 1:
        return False
    return True

bl = False
for p in gen_pair_pattern(H):
    if test(p):
        bl = True
        break

answer = 'YES' if bl else 'NO'
print(answer)

import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return list(map(int, sys.stdin.readline().split()))
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
import itertools

N, *A = mi()
L = [ii() for _ in range(N)]

#A = sorted(A)
sum_a = sum(A)

def dfs(i, a, b, c, use):
    if (0 not in [a, b, c]) and use > 2:
        nonlocal ans
        #abc = sorted([a, b, c])
        #ans = min(ans, (use-3)*10 + sum([abs(abc[i]-A[i]) for i in range(3)]))
        ans = min(ans, (use-3)*10 + abs(a-A[0]) + abs(b-A[1]) + abs(c-A[2]))

    if i > N-1:
        return

    dfs(i+1, a+L[i], b, c, use+1)
    dfs(i+1, a, b+L[i], c, use+1)
    dfs(i+1, a, b, c+L[i], use+1)
    dfs(i+1, a, b, c, use)

ans = float('inf')
dfs(0, 0, 0, 0, 0)

print(ans)



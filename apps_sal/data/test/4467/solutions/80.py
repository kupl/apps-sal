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
'''
N = ii()
A = li2(N)
B = li2(N)

A = sorted(A, key=lambda x:x[0])
B = sorted(B, key=lambda x:x[0])

a_ind = 0
b_ind = 0
cnt = 0

while b_ind < N:
    if A[a_ind][0] < B[b_ind][0] and  A[a_ind][1] < B[b_ind][1]:
        cnt += 1
        a_ind += 1
        b_ind += 1
    else:
        b_ind += 1

print(cnt)
'''
'''
#nonlocal ans
ans = 0

def dfs(a_ind, b_ind, cnt):
    if a_ind >= N or b_ind >= N:
        nonlocal ans
        ans = max(ans, cnt)
        return
    if A[a_ind][0] < B[b_ind][0] and  A[a_ind][1] < B[b_ind][1]:
        dfs(a_ind+1, b_ind+1, cnt+1)
    else:
        dfs(a_ind+1, b_ind, cnt)
        dfs(a_ind, b_ind+1, cnt)
        dfs(a_ind+1, b_ind+1, cnt)

dfs(0, 0, 0)

print(ans)
'''

# XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
#   edges[x]: xとつながるYの頂点のset
#   matched[y]: yとマッチングされたXの頂点(暫定)

def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False
 
 
# 標準入力からのグラフ読み取り
#xn, yn, e = map(int, input().split())
N = ii()
xn = N
yn = N
edges = [set() for _ in range(xn)]
matched = [-1] * yn
 
#for _ in range(e):
    #x, y = map(int, input().split())
    #edges[x].add(y)

A = li2(N)
B = li2(N)

for i in range(N):
    for j in range(N):
        if A[i][0] < B[j][0] and  A[i][1] < B[j][1]:
            edges[i].add(j)
 
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる
print(sum(dfs(s, set()) for s in range(xn)))

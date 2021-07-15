import sys
import math

#https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

class Node:
    def __init__(self):
        self.edge = []
        self.count = 0

def dfs(tree,node,p_node,p_count,counts):
    count = tree[node].count + p_count
    counts[node] = count
    for x in tree[node].edge:
        if x == p_node:
            continue
        dfs(tree,x,node,count,counts)

N,Q = inm()

tree = []
for _ in range(N):
    tree.append(Node())

#node = Node()
#tree = [node]*N

for _ in range(N-1):
    a,b = inm()
    tree[a-1].edge.append(b-1)
    tree[b-1].edge.append(a-1)

for _ in range(Q):
    p,x = inm()
    tree[p-1].count += x

val = []
for _ in range(N):
    val.append(0)

#for i in range(N):
#    print(tree[i].edge)
#    print(tree[i].count)

dfs(tree,0,-1,0,val)

counts_str = [str(n) for n in val]
s = " ".join(counts_str)
print(s)


import collections
import sys
input = sys.stdin.readline
def N(): return int(input())
def NM(): return map(int, input().split())
def L(): return list(NM())
def LN(n): return [N() for i in range(n)]
def LL(n): return [L() for i in range(n)]


n = N()
a = L()
b = L()
d = dict()
for i, j in enumerate(a):
    d[j] = i
ans = collections.defaultdict(int)
for i, j in enumerate(b):
    ans[(d[j] - i) % n] += 1
print(max(ans.values()))

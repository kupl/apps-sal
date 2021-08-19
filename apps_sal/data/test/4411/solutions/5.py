"""
template author-: Pyduper
"""
import heapq
import sys


def input():
    return sys.stdin.readline().strip()


maxn = 200005


def lowbit(x):
    return x & -x


def add(t, i, v):
    while i < len(t):
        t[i] += v
        i += lowbit(i)


def sum(t, i):
    ans = 0
    while i > 0:
        ans += t[i]
        i -= lowbit(i)
    return ans


trees = [0] * maxn
(n, k) = map(int, input().split(' '))
seg = []
points = [0] * maxn
cand = []
for i in range(n):
    (l, r) = map(int, input().split(' '))
    seg.append((l, r, i + 1))
    points[l] += 1
    points[r + 1] -= 1
st = 0
for i in range(maxn):
    st += points[i]
    if st > k:
        cand.append((i, st - k))
seg.sort(key=lambda x: (x[0], x[1]))
pq = []
j = 0
ans = []
for (i, v) in cand:
    v = v - sum(trees, i)
    if v <= 0:
        continue
    while j < n and seg[j][0] <= i:
        heapq.heappush(pq, (-seg[j][1], seg[j][0], seg[j][2]))
        j += 1
    for t in range(v):
        (r, l, idx) = heapq.heappop(pq)
        ans.append(idx)
        add(trees, l, 1)
        add(trees, -r + 1, -1)
print(len(ans))
print(*ans)

"""
Created on Oct 6, 2014

@author: nod
"""
(n, m) = map(int, input().split())
horizontal = str(input())
visited = []
h = []
vertical = str(input())
v = []
for char in horizontal:
    if char == '>':
        h.append(int(1))
    else:
        h.append(int(-1))
for char in vertical:
    if char == 'v':
        v.append(int(1))
    else:
        v.append(int(-1))


def travel(ni, mi):
    leftright = h[ni]
    updown = v[mi]
    visited.append([ni, mi])
    newn = ni + updown
    newm = mi + leftright
    if newn >= 0 and newn < n and ([newn, mi] not in visited):
        travel(newn, mi)
    if newm >= 0 and newm < m and ([ni, newm] not in visited):
        travel(ni, newm)
    return visited


def solve():
    lst = [[0, 0], [0, m - 1], [n - 1, 0], [n - 1, m - 1]]
    visited = []
    for l in lst:
        visited.clear()
        vis = travel(l[0], l[1])
        if len(vis) != m * n:
            print('NO')
            return
        visited.clear()
        vis.clear()
    print('YES')


solve()

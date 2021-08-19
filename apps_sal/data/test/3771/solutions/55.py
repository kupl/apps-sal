import scipy.sparse
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


(h, w) = list(map(int, input().split()))
data = []
rs = []
cs = []
for i in range(h):
    c = input()
    if 'S' in c:
        start = (i, c.index('S'))
    if 'T' in c:
        goal = (i, c.index('T'))
    for j in range(w):
        if c[j] in 'o':
            data.append(1)
            rs.append(i)
            cs.append(h + j)
            data.append(1)
            rs.append(h + j)
            cs.append(i)
s = h + w
t = h + w + 1
V = 10 ** 9
data.append(V)
rs.append(s)
cs.append(start[0])
data.append(V)
rs.append(start[0])
cs.append(s)
data.append(V)
rs.append(s)
cs.append(start[1] + h)
data.append(V)
rs.append(start[1] + h)
cs.append(s)
data.append(V)
rs.append(goal[0])
cs.append(t)
data.append(V)
rs.append(t)
cs.append(goal[0])
data.append(V)
rs.append(t)
cs.append(goal[1] + h)
data.append(V)
rs.append(goal[1] + h)
cs.append(t)
m = scipy.sparse.csr_matrix((data, (rs, cs)), shape=(h + w + 2, h + w + 2))
val = scipy.sparse.csgraph.maximum_flow(m, s, t).flow_value
if val >= 10 ** 9:
    val = -1
print(val)

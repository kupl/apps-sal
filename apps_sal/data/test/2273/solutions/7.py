from collections import deque
import sys
input = sys.stdin.readline
n, m = [int(item) for item in input().split()]
ab = []
edges = [[] for _ in range(n)]

for i in range(m):
    a, b = [int(item) for item in input().split()]
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
    ab.append((a, b))


groupA = [1] * n
for a, b in ab:
    if a == 0:
        groupA[b] = 0
    elif b == 0:
        groupA[a] = 0
par = None
for i, item in enumerate(groupA):
    if item == 0:
        par = i
        break
if par == None:
    print(-1)
    return

groupB = [1] * n
for a, b in ab:
    if a == par:
        groupB[b] = 0
    elif b == par:
        groupB[a] = 0

par = None
for i, (p, q) in enumerate(zip(groupA, groupB)):
    if p == 0 and q == 0:
        par = i
        break
if par == None:
    print(-1)
    return

groupC = [1] * n
for a, b in ab:
    if a == par:
        groupC[b] = 0
    elif b == par:
        groupC[a] = 0

# Check edge num
sumA = sum(groupA)
sumB = sum(groupB)
sumC = sum(groupC)
e_abc = [0, n - sumA, n - sumB, n - sumC]
edge_num = sumA * sumB + sumB * sumC + sumC * sumA
if edge_num != m:
    print(-1)
    return

# Answer
setA = set()
setB = set()
setC = set()
group = [groupA, groupB, groupC]
ret = []
for i, (ga, gb, gc) in enumerate(zip(groupA, groupB, groupC)):
    total = ga + gb + gc
    if total != 1:
        print(-1)
        return
    if ga:
        ret.append(1)
        setA.add(i)
    elif gb:
        ret.append(2)
        setB.add(i)
    else:
        ret.append(3)
        setC.add(i)
s_ABC = [set(), setA, setB, setC]
for i, item in enumerate(ret):
    if e_abc[item] != len(edges[i]):
        print(-1)
        return
    for node in edges[i]:
        if node in s_ABC[item]:
            print(-1)
            return
print(" ".join([str(item) for item in ret]))

import sys

class Node:
    def __init__(self, d):
        nonlocal nodes
        self.ch = {}
        self.a = [[], []]
        self.d = d
        nodes += [self]

nodes = []
pairs = []
res = 0

N = int(sys.stdin.readline())
_input = sys.stdin.readlines()
_input = [s[:-1] for s in _input]
A = [_input[:N], _input[N:]]
T = Node(0)

for i, l in enumerate(A):
    for j, s in enumerate(l):
        t = T
        for c in s:
            v = ord(c) - ord('a')
            if not v in t.ch:
                t.ch[v] = Node(t.d + 1)
            t = t.ch[v]
        t.a[i] += [j + 1]

for n in reversed(nodes):
    for i in n.ch:
        n.a[0] += n.ch[i].a[0]
        n.a[1] += n.ch[i].a[1]
    k = min(len(n.a[0]), len(n.a[1]))
    for i in range(k):
        pairs += [str(n.a[0][-1]) + ' ' + str(n.a[1][-1])]
        n.a[0].pop()
        n.a[1].pop()
        res += n.d

print(res)
print('\n'.join(pairs))


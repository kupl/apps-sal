n = int(input())
t = {}


class node(object):
    """docstring for node"""

    def __init__(self):
        self.vois = []

    def insv(self, voi):
        self.vois.append(voi)


for i in range(1, n + 1):
    t[i] = node()
for i in range(n - 1):
    (u, v) = map(int, input().split())
    t[u].insv(v)
    t[v].insv(u)
for i in range(1, n + 1):
    if len(t[i].vois) == 2:
        print('NO')
        break
else:
    print('YES')

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def append(self, v):
        v += 1
        nd = self.root
        while True:
            if v == nd.value:

                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left:
            return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right:
            return self.rightmost(nd.right)
        return nd

    def find_l(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v:
            prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v:
            prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1 << self.N) - 1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None):
        v += 1
        if not nd:
            nd = self.root
        if not prev:
            prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None


n = int(input())
s = input()

alice = [int(s[i] == "0") for i in range(n)]
bob = [int(s[i] == "1") for i in range(n)]
for i in range(1, n):
    alice[i] += alice[i - 1]
    bob[i] += bob[i - 1]
alice.append(0)
bob.append(0)

update_que = [[] for i in range(n)]

alice_win = []
id = 0
while id < n:
    if s[id] != "0":
        pos = id
        while pos < n and s[pos] != "0":
            pos += 1
        update_que[pos - id - 1].append(id)
        id = pos
    else:
        id += 1
bob_win = []
id = 0
while id < n:
    if s[id] != "1":
        pos = id
        while pos < n and s[pos] != "1":
            pos += 1
        update_que[pos - id - 1].append(id)
        id = pos
    else:
        id += 1

bst = BalancingTree(20)
bst.append(n)

ans = [0] * n
for i in range(n - 1, -1, -1):
    for id in update_que[i]:
        bst.append(id)
    pos = 0
    res = 0
    while pos < n - i:
        check1 = alice[pos + i] - alice[pos - 1]
        check2 = bob[pos + i] - bob[pos - 1]
        if not check1 or not check2:
            res += 1
            pos += i + 1
        else:
            npos = bst.find_r(pos - 1)
            if npos == n:
                break
            else:
                pos = npos + i + 1
                res += 1
    ans[i] = res

print(*ans)

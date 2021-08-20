from collections import deque


class Treap:

    def __init__(self, key, priority, prrty_cmprtr):
        self.key = key
        self.priority = priority
        self.priority_comparator = prrty_cmprtr
        self.left = None
        self.right = None

    def merge(self, right):
        if right is None:
            return self
        if self.priority_comparator(self.priority, right.priority):
            root = self
            if root.right is not None:
                root.right = root.right.merge(right)
            else:
                root.right = right
        else:
            root = right
            root.left = self.merge(right.left)
        return root

    def split(self, key):
        if self.key <= key:
            left = self
            if left.right is not None:
                (left.right, right) = left.right.split(key)
            else:
                (left.right, right) = (None, None)
        else:
            right = self
            if right.left is not None:
                (left, right.left) = right.left.split(key)
            else:
                (left, right.left) = (None, None)
        return (left, right)

    def insert(self, element):
        (left, right) = self.split(element.key)
        if left is not None:
            t = left.merge(element)
        else:
            t = element
        if right is not None:
            return t.merge(right)
        return t

    def delete(self, key):
        (left, right) = self.split(key)
        (left, middle) = left.split(key - 1)
        if left is not None:
            return left.merge(right)
        return right

    def find(self, key):
        pos = self
        while True:
            if key == pos.key:
                return True
            elif key < pos.key:
                if pos.left is None:
                    return False
                pos = pos.left
            else:
                if pos.right is None:
                    return False
                pos = pos.right


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
first = [deque() for i in range(n)]
for i in range(n):
    first[a[i] - 1].append(i)
first[a[0] - 1].popleft()
if not first[a[0] - 1]:
    priority = float('inf')
else:
    priority = first[a[0] - 1][0]
treap = Treap(a[0], priority, lambda x, y: x >= y)
(l, res) = (1, 1)
for i in range(1, n):
    first[a[i] - 1].popleft()
    if not first[a[i] - 1]:
        priority = float('inf')
    else:
        priority = first[a[i] - 1][0]
    if not treap.find(a[i]):
        if l == k:
            treap = treap.delete(treap.key)
            l -= 1
        if treap is not None:
            treap = treap.insert(Treap(a[i], priority, lambda x, y: x >= y))
        else:
            treap = Treap(a[i], priority, lambda x, y: x >= y)
        l += 1
        res += 1
    else:
        treap = treap.delete(a[i])
        if treap is not None:
            treap = treap.insert(Treap(a[i], priority, lambda x, y: x >= y))
        else:
            treap = Treap(a[i], priority, lambda x, y: x >= y)
print(res)

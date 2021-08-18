class Node:
    def __init__(self, key=None):

        self.key = key
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None


def update_height(t):
    if t.left is not None:
        l = t.left.height
    else:
        l = 0
    if t.right is not None:
        r = t.right.height
    else:
        r = 0

    if l >= r:
        t.height = l + 1
    else:
        t.height = r + 1


class AVL:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        if self.root.key is None:
            self.root.key = key
            return
        cursor = self.root
        while cursor:
            p = cursor
            if key == cursor.key:
                return
            elif key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        new_node = Node(key)
        new_node.parent = p
        if key < p.key:
            p.left = new_node
        else:
            p.right = new_node

        cursor = p
        while cursor:
            if cursor.left is not None:
                l = cursor.left.height
            else:
                l = 0
            if cursor.right is not None:
                r = cursor.right.height
            else:
                r = 0
            balance = l - r

            if balance == 0:
                break
            elif balance == 2:
                if key < cursor.left.key:
                    self.rotate_r(cursor)
                else:
                    self.rotate_lr(cursor)
                break
            elif balance == -2:
                if key > cursor.right.key:
                    self.rotate_l(cursor)
                else:
                    self.rotate_rl(cursor)
                break
            else:
                update_height(cursor)
                cursor = cursor.parent

    def rotate_r(self, n):
        p = n.parent
        c = n.left
        gc = n.left.right

        if gc is not None:
            n.left = gc
            gc.parent = n
        else:
            n.left = None

        c.right = n
        n.parent = c

        if p is not None:
            if p.right == n:
                p.right = c
            else:
                p.left = c
            c.parent = p
        else:
            self.root = c
            self.root.parent = None

        update_height(n)
        update_height(c)

    def rotate_l(self, n):
        p = n.parent
        c = n.right
        gc = n.right.left

        if gc is not None:
            n.right = gc
            gc.parent = n
        else:
            n.right = None

        c.left = n
        n.parent = c

        if p is not None:
            if p.left == n:
                p.left = c
            else:
                p.right = c
            c.parent = p
        else:
            self.root = c
            self.root.parent = None

        update_height(n)
        update_height(c)

    def rotate_rl(self, n):

        p = n.parent
        c = n.right
        gc = n.right.left

        if gc.left and gc.right:
            n.right = gc.left
            c.left = gc.right
            gc.left.parent = n
            gc.right.parent = c
        elif gc.left:
            n.right = gc.left
            gc.left.parent = n
            c.left = None
        elif gc.right:
            c.left = gc.right
            gc.right.parent = c
            n.right = None
        else:
            n.right = None
            c.left = None

        gc.left = n
        gc.right = c
        n.parent = gc
        c.parent = gc

        if p is not None:
            if p.left == n:
                p.left = gc
            else:
                p.right = gc
            gc.parent = p
        else:
            self.root = gc
            self.root.parent = None

        update_height(n)
        update_height(c)
        update_height(gc)

    def rotate_lr(self, n):
        p = n.parent
        c = n.left
        gc = n.left.right

        if gc.left and gc.right:
            c.right = gc.left
            n.left = gc.right
            gc.left.parent = c
            gc.right.parent = n
        elif gc.left:
            c.right = gc.left
            gc.left.parent = c
            n.left = None
        elif gc.right:
            n.left = gc.right
            gc.right.parent = n
            c.right = None
        else:
            n.left = None
            c.right = None
        gc.left = c
        gc.right = n
        c.parent = gc
        n.parent = gc

        if p is not None:
            if p.left == n:
                p.left = gc
            else:
                p.right = gc
            gc.parent = p
        else:
            self.root = gc
            self.root.parent = None

        update_height(n)
        update_height(c)
        update_height(gc)

    def find(self, key):
        cursor = self.root
        while cursor:
            if cursor.key == key:
                return cursor
            if key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        return None

    def next_greater_key(self, cursor):
        if cursor is None:
            return None
        if cursor.right:
            cursor = cursor.right
            while cursor.left:
                cursor = cursor.left
            return cursor
        elif cursor.parent.left == cursor:
            return cursor.parent
        elif cursor.parent.right == cursor:
            while cursor.parent and cursor.parent.right == cursor:
                cursor = cursor.parent
            if cursor.parent:
                return cursor.parent
        else:
            return None

    def next_smaller_key(self, cursor):
        if cursor is None:
            return None
        if cursor.left:
            cursor = cursor.left
            while cursor.right:
                cursor = cursor.right
            return cursor
        elif cursor.parent.right == cursor:
            return cursor.parent
        elif cursor.parent.left == cursor:
            while cursor.parent and cursor.parent.left == cursor:
                cursor = cursor.parent
            if cursor.parent:
                return cursor.parent
        else:
            return None

    def get_smaller_key(self, key):
        cursor = self.find(key)
        l1 = self.next_smaller_key(cursor)
        l2 = self.next_smaller_key(l1)
        if l2 is None:
            l2 = 0
        else:
            l2 = l2.key
        return l1.key, l2

    def get_greater_key(self, key):
        cursor = self.find(key)
        r1 = self.next_greater_key(cursor)
        r2 = self.next_greater_key(r1)
        if r2 is None:
            r2 = 0
        else:
            r2 = r2.key
        return r1.key, r2


def main():

    N = int(input())
    P = map(int, input().split())

    idx = [-1] * (N + 1)
    for i, v in enumerate(P, 1):
        idx[v] = i
    avl = AVL()
    for i in [0, idx[N], N + 1]:
        avl.insert(i)
    total = 0
    for j in range(N - 1, 0, -1):
        n = idx[j]
        avl.insert(n)

        l1_idx, l2_idx = avl.get_smaller_key(n)
        l1 = n - l1_idx
        if l1_idx != 0:
            l2 = l1_idx - l2_idx
        else:
            l2 = 0

        r1_idx, r2_idx = avl.get_greater_key(n)
        r1 = r1_idx - n
        if r1_idx != N + 1:
            r2 = r2_idx - r1_idx
        else:
            r2 = 0

        cnt = (l1 * r2 + r1 * l2) * j
        total += cnt

    print(total)


def __starting_point():
    main()


__starting_point()

class RedBlackTree():
    _nil = (None, False, None, None, None)

    def __init__(self):
        self._root = RedBlackTree._nil

    def insert_key(self, key):
        y = self.search(key, True)
        z = [key, False, None, None, y]
        if y is RedBlackTree._nil:
            self._root = z
        else:
            y[2 if z[0] < y[0] else 3] = z
        z[2] = z[3] = RedBlackTree._nil
        z[1] = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z[4][1]:
            if z[4] == z[4][4][2]:
                y = z[4][4][3]
                if y[1]:
                    z[4][1] = y[1] = False
                    z[4][4][1] = True
                    z = z[4][4]
                else:
                    if z == z[4][3]:
                        z = z[4]
                        self._left_rotate(z)
                    z[4][1] = False
                    z[4][4][1] = True
                    self._right_rotate(z[4][4])
            else:
                y = z[4][4][2]
                if y[1]:
                    z[4][1] = y[1] = False
                    z[4][4][1] = True
                    z = z[4][4]
                else:
                    if z == z[4][2]:
                        z = z[4]
                        self._right_rotate(z)
                    z[4][1] = False
                    z[4][4][1] = True
                    self._left_rotate(z[4][4])
        self._root[1] = False

    def _left_rotate(self, x):
        y = x[3]
        x[3] = y[2]
        if y[2] is not RedBlackTree._nil:
            y[2][4] = x
        y[4] = x[4]
        if x[4] is RedBlackTree._nil:
            self._root = y
        else:
            x[4][3 - (x == x[4][2])] = y
        y[2] = x
        x[4] = y

    def _right_rotate(self, y):
        x = y[2]
        y[2] = x[3]
        if x[3] is not RedBlackTree._nil:
            x[3][4] = y
        x[4] = y[4]
        if y[4] is RedBlackTree._nil:
            self._root = x
        else:
            y[4][2 + (y == y[4][3])] = x
        x[3] = y
        y[4] = x

    def search(self, key, s):
        x, g = self._root, RedBlackTree._nil
        while x is not RedBlackTree._nil:
            g, x = x, x[2 if key < x[0] else 3]
        return g

    def search2(self, key):
        a = b = None
        x = self._root
        while x is not RedBlackTree._nil and key != x[0]:
            if key < x[0]:
                a, x = x, x[2]
            else:
                b, x = x, x[3]
        if key != x[0]:
            return a, b


def main():
    input()
    a, *aa = list(map(int, input().split()))
    t = RedBlackTree()
    t.insert_key([a, 0, 0])
    e = []
    for a in aa:
        o, u = t.search2([a, 0, 0])
        if u is None:
            e.append(o[0][0])
            o[0][2 - (o[0][0] > a)] = 1
        elif o is None:
            e.append(u[0][0])
            u[0][2 - (u[0][0] > a)] = 1
        else:
            if o[0][0] > a < u[0][0]:
                if o[0][1] == 0:
                    o[0][1] = 1
                    e.append(o[0][0])
                else:
                    u[0][1] = 1
                    e.append(u[0][0])
            elif o[0][0] < a < u[0][0]:
                if o[0][2]:
                    u[0][1] = 1
                    e.append(u[0][0])
                else:
                    o[0][2] = 1
                    e.append(o[0][0])
            elif o[0][0] > a > u[0][0]:
                if o[0][1]:
                    u[0][2] = 1
                    e.append(u[0][0])
                else:
                    o[0][1] = 1
                    e.append(o[0][0])
            elif o[0][0] < a > u[0][0]:
                if o[0][2]:
                    u[0][2] = 1
                    e.append(u[0][0])
                else:
                    o[0][2] = 1
                    e.append(o[0][0])
        t.insert_key([a, 0, 0])
    print(*e)


def __starting_point():
    main()

__starting_point()

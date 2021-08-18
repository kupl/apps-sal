

class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.dat = [0] * (size + 1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i

    def sum(self, r):
        r += 1
        ret = 0
        while r > 0:
            ret += self.dat[r]
            r -= r & -r
        return ret

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def get_original_sequence(self):
        ret = self.get_aggrigate_sequence()
        for i in range(self.size - 1, 0, -1):
            ret[i] -= ret[i - 1]
        return ret

    def get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self.get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self.get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret


n, q = list(map(int, input().split()))
cx = BinaryIndexedTree(n + 1)
cy = BinaryIndexedTree(n + 1)
cx.add(1, n - 2)
cy.add(1, n - 2)
mx, my = n, n
ret = pow(n - 2, 2)
for _ in range(q):
    u, v = list(map(int, input().split()))
    if u == 1:
        ret -= cx.sum(v)
        if mx > v:
            cy.add(1, v - mx)
            cy.add(my, mx - v)
            mx = v
    else:
        ret -= cy.sum(v)
        if my > v:
            cx.add(1, v - my)
            cx.add(mx, my - v)
            my = v

print(ret)

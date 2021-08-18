import collections

max_bits = 30


class BNode:
    def __init__(self, ct=0, zero=None, one=None):
        self.ct = ct
        self.zero = None
        self.one = None

    def __str__(self):
        return ' '.join([str(self.ct), str(self.zero), str(self.one)])


root = BNode()


def bits(x):
    bit = 2**(max_bits - 1)
    for i in range(max_bits):
        if x & bit:
            yield 1
        else:
            yield 0
        bit >>= 1


def add(x, root):
    root.ct += 1
    for b in bits(x):
        if b:
            if not root.one:
                root.one = BNode()
            root = root.one
        else:
            if not root.zero:
                root.zero = BNode()
            root = root.zero
        root.ct += 1


def sub(x, root):
    root.ct -= 1
    for b in bits(x):
        if b:
            if root.one.ct == 1:
                root.one = None
                break
            root = root.one
        else:
            if root.zero.ct == 1:
                root.zero = None
                break
            root = root.zero
        root.ct -= 1


def question(x, root):
    y = 0
    for b in bits(x):
        if b:
            if root.zero and root.zero.ct > 0:
                root = root.zero
                y = y * 2
            else:
                root = root.one
                y = y * 2 + 1
        else:
            if root.one and root.one.ct > 0:
                root = root.one
                y = y * 2 + 1
            else:
                root = root.zero
                y = y * 2
    return x ^ y


add(0, root)

q = int(input())

output = []

for i in range(q):
    qtype, x = input().split()
    x = int(x)
    if qtype == '+':
        add(x, root)
    if qtype == '-':
        sub(x, root)
    if qtype == '?':
        output.append(str(question(x, root)))

print("\n".join(output))

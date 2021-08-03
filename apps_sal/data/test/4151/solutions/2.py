class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default", "op"]

    def __init__(self, a: list, default: int, op):
        import math
        real_size = len(a)
        self.elem_size = elem_size = 1 << math.ceil(math.log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op

        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

    def get_value(self, x: int, y: int) -> int:
        l, r = x + self.elem_size, y + self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
            l, r = l >> 1, r >> 1

        return result

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int) -> None:
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])


def __starting_point():
    from collections import defaultdict
    N = int(input())
    a = list(map(int, input().split()))
    index_dict = defaultdict(list)
    for i, n in enumerate(a):
        index_dict[n].append(i)

    last_num = 0
    ans = []
    append = ans.append
    segtree = SegmentTree([10**6] * (N + 1), 10**6, min)
    getv, setv = segtree.get_value, segtree.set_value

    for i, n in enumerate(a):
        if not index_dict[n]:
            continue
        last_num = min(last_num + 1, getv(i + 1, N + 1))
        for j in index_dict[n]:
            setv(j, last_num)
        append(last_num)
        index_dict[n] = []

    mod = 998244353

    ans = pow(2, len(set(ans)) - 1, mod)
    print(ans)


__starting_point()

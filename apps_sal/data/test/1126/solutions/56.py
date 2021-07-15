class DoublingAggregation:
    def __init__(self, nexts, arr, max_n, op, e):
        # op はモノイド
        n = len(nexts)
        self.table = [nexts[:]]
        self.data = [arr[:]]
        self.op = op
        self.e = e
        self.max_n = max_n
        for k in range(max_n.bit_length()-1):
            perm = self.table[-1]
            perm_next = []
            dat = self.data[-1]
            dat_next = []
            for p, d in zip(perm, dat):
                perm_next.append(perm[p])  # perm[p] == perm[perm[idx_perm]]
                dat_next.append(op(d, dat[p]))
            self.table.append(perm_next)
            self.data.append(dat_next)

    def prod(self, idx, n):
        # arr[idx] * arr[nexts[idx]] * arr[nexts[nexts[idx]] * ... を n 回繰り替えした値を返す
        val = self.e
        op = self.op
        for bit, (t, dat) in enumerate(zip(self.table, self.data)):
            if n >> bit & 1:
                val = op(val, dat[idx])
                idx = t[idx]
        return idx, val

    def max_right(self, idx, f):
        # f(arr[idx] * arr[nexts[idx]] * arr[nexts[nexts[idx]] * ... (n 回)) が
        # True である最大の n と、そのときの prod(idx, n)
        n = 0
        val = self.e
        op = self.op
        for bit, t, dat in zip(list(range(len(self.table)-1, -1, -1)), self.table[::-1], self.data[::-1]):
            val_next = op(val, dat[idx])
            if f(val_next):
                val = val_next
                idx = t[idx]
                n |= 1 << bit
        if n > self.max_n:
            n = self.max_n
        return n, idx, val


from operator import add

N, X, M = list(map(int, input().split()))
nexts = [i*i%M for i in range(M)]
arr = list(range(M))
doubling = DoublingAggregation(nexts, arr, N, add, 0)
ans = doubling.prod(X, N)[1]
print(ans)


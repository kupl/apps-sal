class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        self.ret = 0
        record = {}
        disjoint = [-1] * len(A)

        def find(x):
            idx = x
            while disjoint[idx] >= 0:
                idx = disjoint[idx]
            while disjoint[x] >= 0:
                tmp = disjoint[x]
                disjoint[x] = idx
                x = tmp
            return idx

        def union(a, b):
            if a == b:
                return
            a_idx = find(a)
            b_idx = find(b)
            if a_idx == b_idx:
                return
            disjoint[a_idx] += disjoint[b_idx]
            disjoint[b_idx] = a_idx
            self.ret = min(self.ret, disjoint[a_idx])

        def factor(x, idx):
            if x < 3:
                union(record.get(x, idx), idx)
                record[x] = idx
                return
            if x % 2 == 0:
                union(record.get(2, idx), idx)
                record[2] = idx
                while x % 2 == 0:
                    x = x // 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    union(record.get(i, idx), idx)
                    record[i] = idx
                while x % i == 0:
                    x = x // i
                i += 2
            if x > 1:
                union(record.get(x, idx), idx)
                record[x] = idx
        factors = [factor(A[i], i) for i in range(len(A))]
        return -self.ret

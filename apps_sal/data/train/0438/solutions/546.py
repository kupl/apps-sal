

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr) + 2

        tree = [0] * (2 * N)

        def build(arr):

            for i in range(n):
                tree[n + i] = arr[i]

            for i in range(n - 1, 0, -1):
                tree[i] = tree[i << 1] + tree[i << 1 | 1]

        def updateTreeNode(p, value):

            tree[p + n] = value
            p = p + n

            i = p

            while i > 1:

                tree[i >> 1] = tree[i] + tree[i ^ 1]
                i >>= 1

        def query(l, r):

            res = 0

            l += n
            r += n

            while l < r:

                if (l & 1):
                    res += tree[l]
                    l += 1

                if (r & 1):
                    r -= 1
                    res += tree[r]

                l >>= 1
                r >>= 1

            return res

        if m == len(arr):
            return len(arr)

        n = len(arr) + 2
        init = [0] * (n + 1)
        init[0] = init[n - 1] = 1
        build(init)
        for i in range(len(arr) - 1, -1, -1):
            e = arr[i]
            print(e)
            if 0 <= e - (m + 1) and init[e - (m + 1)] == 1 and query(e - m, e) == 0:
                return i
            if e + (m + 1) <= n - 1 and init[e + (m + 1)] == 1 and query(e, e + m + 1) == 0:
                return i
            updateTreeNode(e, 1)
            init[e] = 1
        return -1

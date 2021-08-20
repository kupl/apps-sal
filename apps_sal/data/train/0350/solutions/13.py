class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        length = len(A)

        class counter:

            def __init__(self):
                self.c = Counter()

            def addValue(self, num):
                self.c[num] += 1

            def removeValue(self, num):
                self.c[num] -= 1
                if self.c[num] == 0:
                    del self.c[num]

        def subarraysWithAtLeast(k):
            start = 0
            c = counter()
            ret = 0
            for i in range(length):
                cur = A[i]
                c.addValue(cur)
                if len(c.c) < k:
                    ret += i - start + 1
                    continue
                while len(c.c) > k:
                    tmp = A[start]
                    c.removeValue(tmp)
                    start += 1
                assert len(c.c) == k
                ret += i - start + 1
            return ret
        return subarraysWithAtLeast(K) - subarraysWithAtLeast(K - 1)

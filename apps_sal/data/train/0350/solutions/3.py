class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # seems like you need 3 pointers, shink from either side
        ans, ctr, lb, count = 0, {}, 0, 0
        for i, val in enumerate(A):
            if val not in ctr:
                ctr[val] = 0
            ctr[val] += 1

            # try to code it up first
            while len(ctr) > K:
                ctr[A[lb]] -= 1
                if ctr[A[lb]] == 0:
                    del ctr[A[lb]]
                lb += 1

            if len(ctr) == K:
                p2, count, ctr1 = lb, 0, collections.Counter()
                while len(ctr) == K:
                    count += 1
                    ctr[A[p2]] -= 1
                    if ctr[A[p2]] == 0:
                        del ctr[A[p2]]
                    ctr1[A[p2]] += 1
                    p2 += 1
                ans += count
                for k, v in ctr1.items():
                    # recover step, kind of lame
                    ctr[k] = ctr.get(k, 0) + v
        return ans


class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans

class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        a = [0] * len(arr)
        heads = {}
        ends = {}
        ans = -1
        for (step, i) in enumerate(arr):
            a[i - 1] = 1
            if self.mergeOne(a, i - 1, heads, ends, m) == 1:
                ans = step
        for i in heads:
            if heads[i] - i + 1 == m:
                return len(arr)
        return ans

    def mergeOne(self, ls, index, heads, ends, m):
        (left, right) = (index - 1, index + 1)
        lefthead = rightend = index
        ext = -1
        if left in ends:
            lefthead = ends[left]
            if left - lefthead + 1 == m:
                ext = 1
            del ends[left]
        if right in heads:
            rightend = heads[right]
            if rightend - right + 1 == m:
                ext = 1
            del heads[right]
        heads[lefthead] = rightend
        ends[rightend] = lefthead
        return ext

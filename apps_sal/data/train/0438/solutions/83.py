class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        left = {}
        right = {}
        tot = {}
        cands = set()
        N = len(A)
        res = -1
        for i, a in enumerate(A):
            size = 1
            newLeft = newRight = a
            if a - 1 in tot:
                size += tot[a - 1]
            if a + 1 in tot:
                size += tot[a + 1]
            if a - 1 in tot:
                for c in [a - 1, left[a - 1]]:
                    if c in cands:
                        cands.remove(c)
                newLeft = left[a - 1]
                right[left[a - 1]] = right[a + 1] if a + 1 in tot else a
                tot[left[a - 1]] = size
            if a + 1 in tot:
                for c in [a + 1, right[a + 1]]:
                    if c in cands:
                        cands.remove(c)
                newRight = right[a + 1]
                left[right[a + 1]] = left[a - 1] if a - 1 in tot else a
                tot[right[a + 1]] = size
            tot[a] = size
            left[a] = newLeft
            right[a] = newRight
            if size == m:
                cands.add(newLeft)
                cands.add(newRight)
            if cands:
                res = i + 1
        return res

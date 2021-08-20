class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        ranges = [None for _ in range(len(arr))]
        lefts = set([])
        best = -1
        for (rnd, flipped) in enumerate(arr):
            i = flipped - 1
            left = right = i
            if i > 0 and ranges[i - 1] is not None:
                left = ranges[i - 1][0]
                if left in lefts:
                    lefts.remove(left)
            if i < len(ranges) - 1 and ranges[i + 1] is not None:
                right = ranges[i + 1][1]
                if ranges[i + 1][0] in lefts:
                    lefts.remove(ranges[i + 1][0])
            ranges[i] = [left, right]
            ranges[left] = [left, right]
            ranges[right] = [left, right]
            if right - left + 1 == m:
                lefts.add(left)
            if len(lefts) > 0:
                best = rnd + 1
        return best

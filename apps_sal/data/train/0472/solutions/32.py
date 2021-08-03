class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()

        def canReachRec(ix):
            if ix < 0 or ix >= len(arr):
                return False
            if ix in seen:
                return False
            if arr[ix] == 0:
                return True

            seen.add(ix)
            if canReachRec(ix + arr[ix]):
                return True
            if canReachRec(ix - arr[ix]):
                return True
            return False
        return canReachRec(start)

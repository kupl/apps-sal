class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        store = set([0])
        s = 0
        count = 0
        for i in nums:
            s += i
            if s - target in store:
                count += 1
                store.clear()
            store.add(s)
        return count

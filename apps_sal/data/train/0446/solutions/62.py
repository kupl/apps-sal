class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for num in arr:
            if num not in count:
                count[num] = 0
            count[num] += 1

        values = sorted([v for v in count.values()])
        for _ in range(k):
            values[0] -= 1
            if values[0] == 0:
                del values[0]
        return len(values)

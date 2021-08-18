class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counts = collections.Counter(A)
        count = 0
        A.sort()
        for num in A:
            if counts[num] and counts[num * 2]:
                counts[num * 2] -= 1
                counts[num] -= 1
                count += 1
        return count * 2 == len(A)

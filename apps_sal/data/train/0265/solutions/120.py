class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sums = [0]
        # prefix sum
        for num in nums:
            sums.append(sums[-1] + num)

        # two sum
        hashmap = {}
        results = []
        for i, s in enumerate(sums):
            if s in hashmap:
                start = hashmap[s]
                results.append((start, i - 1))
            need = s + target
            hashmap[need] = i

        prevEnd = -1
        count = 0
        for start, end in results:
            if start > prevEnd:
                count += 1
                prevEnd = end
        return count

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        def max_len(nums):
            negs = [i for i, x in enumerate(nums) if x < 0]
            n = len(nums)

            if len(negs) % 2 == 0:
                return n
            else:
                return max(n - (negs[0] + 1), negs[-1])

        from copy import deepcopy
        chunks = []

        chunk = []
        for x in nums:
            if x == 0 and chunk:
                chunks.append(deepcopy(chunk))
                chunk.clear()
            elif x:
                chunk.append(x)
        chunks.append(chunk)
        print(chunks)

        return max(map(max_len, chunks))

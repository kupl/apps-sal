class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = {0: 1}
        prefix = 0
        result = 0
        for a in A:
            prefix = prefix + a
            if prefix - S in count:
                result += count[prefix - S]
            if prefix in count:
                count[prefix] += 1
            else:
                count[prefix] = 1
        return result

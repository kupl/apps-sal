class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hashmap = [0] * K
        hashmap[0] = 1
        result = 0
        prefix = 0
        for i in range(len(A)):
            prefix = (prefix + A[i]) % K
            hashmap[prefix] += 1
            result += hashmap[prefix] - 1
        return result

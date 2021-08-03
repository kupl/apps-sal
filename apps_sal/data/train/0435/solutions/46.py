class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hm = {}
        hm[0] = 1
        prefix = 0
        count = 0
        for i in range(0, len(A)):
            prefix = (A[i] + prefix) % K
            if prefix in hm:
                count += hm[prefix]
            else:
                hm[prefix] = 0
            hm[prefix] += 1
        return count

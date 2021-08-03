class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hash_map = collections.defaultdict(int)
        hash_map[0] = 1
        prefix = 0
        res = 0
        for i in range(len(A)):
            num = A[i]
            prefix = (prefix + num) % K
            res += hash_map[prefix]
            hash_map[prefix] += 1
        return res

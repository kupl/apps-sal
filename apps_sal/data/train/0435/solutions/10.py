class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        curr_sum = 0
        result = 0
        for a in A:
            curr_sum += a
            remainder = curr_sum % K
            if remainder in m:
                result += m[remainder]
            m[remainder] += 1
        return result

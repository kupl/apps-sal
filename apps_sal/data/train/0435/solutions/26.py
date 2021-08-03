class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = [0] * K
        sum = 0
        for i in A:
            sum += i % K
            count[sum % K] += 1
        result = count[0]
        for j in count:
            result += (j * (j - 1)) / 2
        return int(result)

import collections


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        counts = [0] * K

        total = 0

        for num in A:
            total += num
            counts[total % K] += 1

        result = counts[0]

        for count in counts:
            result += (count * (count - 1)) // 2

        return result

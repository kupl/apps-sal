'''
Contiguous sub array
Positive and negative
cannot be empty

return count


Create prefix

Loop through --> if remainder in prefix count += 1
add prefix % k into seen


4 9 9 7 4 5

4 4 4 5 4 0
'''
from collections import Counter


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        seen = Counter()

        prefix = []
        curr_sum = 0
        for x in A:
            curr_sum += x
            prefix.append(curr_sum % K)

        ans = 0
        for ix in range(len(A)):
            remainder = K - prefix[ix]
            if prefix[ix] in seen:
                ans += seen[prefix[ix]]
            if prefix[ix] == 0:
                ans += 1
            seen[prefix[ix]] += 1
        return ans

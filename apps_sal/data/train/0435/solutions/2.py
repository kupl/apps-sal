class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        B = [a % K for a in A]

        sum_dict = {}
        ans = 0
        curr_sum = 0
        sum_dict[0] = 1

        n = len(B)

        for i, num in enumerate(B):
            curr_sum = (curr_sum + num) % K
            if curr_sum in sum_dict:
                ans += sum_dict[curr_sum]

            sum_dict[curr_sum] = sum_dict.get(curr_sum, 0) + 1

        return ans

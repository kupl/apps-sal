class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction = sorted(satisfaction)
        ans = 0

        for i, s in enumerate(satisfaction):

            index = i
            curr_ans = 0
            j = 1

            while index <= len(satisfaction) - 1:
                curr_ans += j * satisfaction[index]
                j += 1
                index += 1

            ans = max(ans, curr_ans)

        return ans

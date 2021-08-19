class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:

        def cumulative_sum(input_list):
            (curSum, cumSum) = (0, [])
            for i in input_list:
                curSum += i
                cumSum.append(curSum)
            return cumSum
        cumSum = cumulative_sum(light)
        cumSum_target = cumulative_sum(list(range(1, len(light) + 1)))
        return sum([cumSum[i] == cumSum_target[i] for i in range(len(cumSum))])

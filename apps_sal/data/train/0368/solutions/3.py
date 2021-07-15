class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        positive_sum, positive_step, positive_count = 0, 0, 0
        for i in satisfaction:
            if i < 0:
                continue
            positive_count += 1
            positive_sum += positive_count*i
            positive_step += i

        negative_count = len(satisfaction) - positive_count
        result = [positive_sum]
        for i in range(negative_count):

            negative_sum = 0
            for j in range(i+1):
                negative_sum += satisfaction[negative_count-j-1]*(i-j+1)
            result.append(negative_sum + positive_sum + positive_step*(i+1))

        return max(result)

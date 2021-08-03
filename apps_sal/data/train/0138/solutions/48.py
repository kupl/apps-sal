class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positives = 0
        negatives = 0
        output = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                positives += 1

                if negatives > 0:
                    negatives += 1

            elif nums[i] < 0:
                if negatives > 0:
                    tmp = positives
                    positives = negatives + 1
                    negatives = tmp + 1

                else:
                    negatives = positives + 1
                    positives = 0

            else:
                positives = 0
                negatives = 0

            output = max(output, positives)

        return output

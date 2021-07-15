class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        positive = [0 for _ in range(len(arr))]
        negative = positive.copy()
        positive[0] = arr[0]
        for i, num in enumerate(arr[1:]):
            positive[i+1] = max(num, positive[i] + num)
            negative[i+1] = max(negative[i] + num, positive[i])
        return max(positive+negative[1:])
            


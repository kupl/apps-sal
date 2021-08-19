class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n, window_sum = len(customers), 0
        for i in range(n):
            if i < X:
                window_sum += customers[i]
            else:
                window_sum += (1 - grumpy[i]) * customers[i]

        result = window_sum  # 求得指針未滑動前總和
        left, right = 0, X

        while right < n:
            if grumpy[right] == 1:
                window_sum += customers[right]
            if grumpy[left] == 1:
                window_sum -= customers[left]
            result = max(result, window_sum)
            left += 1
            right += 1

        return result

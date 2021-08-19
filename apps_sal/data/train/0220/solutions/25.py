class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        cnt = 0
        acc = [0]
        for i in range(n):
            if grumpy[i]:
                acc.append(acc[-1] + customers[i])
            else:
                acc.append(acc[-1])
                cnt += customers[i]
        ans = cnt
        for i in range(n - X + 1):
            ans = max(ans, cnt + acc[i + X] - acc[i])
        return ans

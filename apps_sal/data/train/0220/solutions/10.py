class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        inital_sum = 0
        tmp_sum = 0
        res_sum = 0
        length = len(customers)
        for i in range(0, len(customers)):
            if grumpy[i] == 0:
                inital_sum += customers[i]
        tmp_sum = inital_sum
        for j in range(0, X):
            if grumpy[j] == 1:
                tmp_sum = tmp_sum + customers[j]
        res_sum = max(tmp_sum, res_sum)
        k = 1
        while k + X - 1 < length:
            if grumpy[k - 1] == 1:
                tmp_sum = tmp_sum - customers[k - 1]
            if grumpy[k + X - 1] == 1:
                tmp_sum = tmp_sum + customers[k + X - 1]
            k += 1
            res_sum = max(tmp_sum, res_sum)
        return res_sum

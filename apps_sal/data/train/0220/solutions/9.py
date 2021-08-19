class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if X > len(customers):
            return sum(customers)
        sum1 = [customers[0]]
        sum2 = []
        if grumpy[0] == 0:
            sum2.append(customers[0])
        else:
            sum2.append(0)
        for i in range(1, len(customers)):
            sum1.append(sum1[-1] + customers[i])
            if grumpy[i] == 0:
                sum2.append(sum2[-1] + customers[i])
            else:
                sum2.append(sum2[-1])
        maxi = sum1[X - 1] + (sum2[-1] - sum2[X - 1])
        for i in range(1, len(customers) - X + 1):
            if sum1[i + X - 1] - sum1[i - 1] + (sum2[-1] - sum2[i + X - 1] + sum2[i - 1]) > maxi:
                maxi = sum1[i + X - 1] - sum1[i - 1] + (sum2[-1] - sum2[i + X - 1] + sum2[i - 1])
        print(sum1, sum2)
        return maxi

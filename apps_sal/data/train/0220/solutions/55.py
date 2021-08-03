class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if X == len(customers):
            return sum(customers)
        for i in range(len(grumpy)):
            grumpy[i] = 0 if grumpy[i] == 1 else 1
        mults = [x * y for x, y in zip(customers, grumpy)]
        sum_not_grumpy = sum(customers[:X])
        not_grumpy = [sum_not_grumpy]
        sum_normal = sum(mults[X:])
        normal_custs = [sum_normal]

        for i in range(1, len(customers) - X + 1):
            sum_not_grumpy -= customers[i - 1]
            sum_not_grumpy += customers[i + X - 1]
            not_grumpy.append(sum_not_grumpy)
            sum_normal += mults[i - 1]
            sum_normal -= mults[i + X - 1]
            normal_custs.append(sum_normal)

        return max([x + y for x, y in zip(not_grumpy, normal_custs)])

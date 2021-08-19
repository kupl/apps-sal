class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base_count = 0
        bonus_array = []
        for (i, j) in zip(customers, grumpy):
            if j == 0:
                base_count += i
            bonus_array.append(i * j)
        bonus = 0
        for i in range(len(customers) - X + 1):
            tmp_bonus = 0
            tmp_bonus = sum(bonus_array[i:i + X])
            bonus = max(bonus, tmp_bonus)
        return base_count + bonus

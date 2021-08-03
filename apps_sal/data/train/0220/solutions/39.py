class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        saved = 0
        max_saved = 0
        sumTotal = 0
        for i, value in enumerate(customers):
            if i - X >= 0 and grumpy[i - X]:
                saved -= customers[i - X]
            if grumpy[i]:
                saved += value
            else:
                sumTotal += value
            max_saved = max(max_saved, saved)
            print((saved, max_saved))
            # print(saved, max_saved, sumTotal)
        return sumTotal + max_saved

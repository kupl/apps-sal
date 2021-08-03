class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)

        start = 0

        curSatisfaction = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        maxSatisfaction = 0

        for end in range(len(customers)):
            if grumpy[end] == 1:
                curSatisfaction += customers[end]

            if end - start + 1 > X:
                if grumpy[start] == 1:
                    curSatisfaction -= customers[start]
                start += 1

            maxSatisfaction = max(maxSatisfaction, curSatisfaction)

        return maxSatisfaction

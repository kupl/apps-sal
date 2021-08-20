class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        without_x = 0
        for (i, b) in enumerate(grumpy):
            if not b:
                without_x += customers[i]
        with_x = [0] * len(customers)
        extra = 0
        for (i, b) in enumerate(grumpy[:X]):
            if b:
                extra += customers[i]
        with_x[0] += extra
        for i in range(len(grumpy)):
            if i + X >= len(grumpy):
                break
            extra -= 0 if not grumpy[i] else customers[i]
            extra += 0 if not grumpy[i + X] else customers[i + X]
            with_x[i + 1] += extra
        return max(with_x) + without_x

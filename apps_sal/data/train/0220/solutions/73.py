class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        zeroTotal = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                zeroTotal += customers[i]

        q = deque()
        oneTotal = 0
        largest = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                while q and i - q[0][1] >= X:
                    oneTotal -= q.popleft()[0]
                q.append((customers[i],i))
                oneTotal += customers[i]
                largest = max(largest, oneTotal)
        return zeroTotal + largest

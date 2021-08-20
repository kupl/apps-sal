class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def isOK(weights, D, w):
            count = 1
            weight = 0
            for i in range(0, len(weights)):
                if weights[i] > w or count > D:
                    return False
                if weight + weights[i] > w:
                    count += 1
                    weight = 0
                weight += weights[i]
            if count <= D:
                return True
            else:
                return False
        left = max(weights)
        right = sum(weights)
        while left <= right:
            middle = (left + right) // 2
            if isOK(weights, D, middle) == True:
                right = middle - 1
            else:
                left = middle + 1
        return left

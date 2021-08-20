class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)

        def possible(c):
            ship = 1
            cargo = 0
            for i in range(len(weights)):
                if ship > D:
                    return False
                if cargo + weights[i] > c:
                    ship += 1
                    cargo = weights[i]
                else:
                    cargo += weights[i]
            return ship <= D
        right = sum(weights)
        while left <= right:
            mid = floor((left + right) / 2)
            if possible(mid):
                if left == mid:
                    break
                right = mid
            else:
                left = mid + 1
        print(left, right, mid)
        return mid

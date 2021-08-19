class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def possible(K):
            # check if it is possible for K bananas to be finished in H hours
            count = 0

            for banana in piles:
                if banana % K == 0:
                    count += banana / K
                else:
                    count += banana // K + 1

            if count <= H:
                return True
            else:
                return False

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            if possible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

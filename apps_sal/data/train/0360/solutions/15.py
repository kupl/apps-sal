class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def test_ship_weights(capacity):
            dq = collections.deque(weights)
            for day in range(D):
                daily_capacity = capacity
                while dq and dq[0] <= daily_capacity:
                    daily_capacity -= dq.popleft()
            if dq:
                return False
            else:
                return True
        (l, r) = (max(weights), sum(weights))
        while l < r:
            m = (l + r) // 2
            if test_ship_weights(m):
                r = m
            else:
                l = m + 1
        return l

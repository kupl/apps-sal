class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # eights.sort()
        left = max(weights)
        right = sum(weights)

        def counter(limit):
            curr = 0
            count = 0
            for w in weights:
                if curr + w == limit:
                    count += 1
                    curr = 0
                elif curr + w > limit:
                    count += 1
                    curr = w
                else:
                    curr += w
            return count if curr == 0 else count + 1

        res = right
        while left <= right:
            mid = (left + right) // 2

            val = counter(mid)
            if val <= D:
                res = min(res, mid)
                right = mid - 1

            else:
                left = mid + 1
                # ight=mid-1
        return res

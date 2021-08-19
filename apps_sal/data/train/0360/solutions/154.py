class Solution:
    def shipWithinDays(self, weights: List[int], limit: int) -> int:

        def count_days(cap: int) -> int:
            cur_weight = 0
            days = 1

            for w in weights:
                if cur_weight + w > cap:
                    days += 1
                    cur_weight = w
                else:
                    cur_weight += w
                # print(f\"cap= {cap}, weight={w}, cur_weight={cur_weight}, days={days}\")

            return days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            time = count_days(mid)
            # print(f\"cap={mid}, left={left}, right={right}, time={time}\")
            if time > limit:
                left = mid + 1
            else:
                right = mid

        return left

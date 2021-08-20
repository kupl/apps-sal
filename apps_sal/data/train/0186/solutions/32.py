class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {val: str(index + 1) for (index, val) in enumerate(cost)}
        cost = sorted(cost_to_digit.keys())

        @lru_cache(None)
        def helper(target: int) -> str:
            if target < cost[0]:
                return None
            max_number = None if target not in cost_to_digit else cost_to_digit[target]
            for c in cost:
                if c > target:
                    break
                curr_number = helper(target - c)
                if curr_number is None:
                    continue
                curr_number = ''.join(sorted(cost_to_digit[c] + curr_number, reverse=True))
                max_number = curr_number if max_number is None or len(curr_number) > len(max_number) or (len(curr_number) == len(max_number) and curr_number > max_number) else max_number
            return max_number
        ans = helper(target)
        return ans if ans else '0'

class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.condition(mid, weights) <= D:
                right = mid
            else:
                left = mid + 1
        return left

    def condition(self, k, weights):
        d = 0
        cur_weight = 0
        for weight in weights:
            if cur_weight + weight == k:
                d += 1
                cur_weight = 0
            elif cur_weight + weight > k:
                d += 1
                cur_weight = weight
            else:
                cur_weight += weight
        return d + 1 if cur_weight > 0 else d
        'def count_days(k, w):\n            curr_wt = 0\n            count = 0\n            for x in weights:\n                if curr_wt+x > k:\n                    count = count+1\n                    cur_wt = x\n                elif curr_wt+x==k:\n                    count=count+1\n                    curr_wt = 0\n                else:\n                    curr_wt = curr_wt+x\n            if curr_wt > 0: return count+1\n            else: return count\n                \n        \n        l = max(weights)\n        r = sum(weights)\n        while l<r:\n            mid = l+((r-l)//2)\n            if count_days(mid, weights) <= D:\n                r = mid\n            else:\n                l = mid+1\n        return l'

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        candidates = collections.Counter(nums)
        keys = list(candidates.keys())
        keys.sort()
        i = 0
        while i < len(keys):
            x = keys[i]
            if candidates[x] == 0:
                i += 1
            else:
                temp = 1
                candidates[x] -= 1
                while temp < k:
                    if candidates[x + temp] > 0:
                        candidates[x + temp] -= 1
                        temp += 1
                    else:
                        return False
        return True

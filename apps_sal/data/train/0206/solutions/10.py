class Solution:

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _cache = {}
        return Solution.Moves(self, nums, 0, len(nums) - 1, 1, _cache) >= 0

    def Moves(self, nums, ini, fin, pl, _cache={}):
        memo = str((ini, fin, pl))
        if memo in list(_cache.keys()):
            return _cache[memo]
        if ini == fin:
            if pl == 1:
                _cache[memo] = nums[ini]
                return _cache[memo]
            else:
                _cache[memo] = -nums[ini]
                return _cache[memo]
        else:
            if pl == 1:
                _cache[memo] = max(Solution.Moves(self, nums, ini + 1, fin, 2, _cache) + nums[ini], Solution.Moves(self, nums, ini, fin - 1, 2, _cache) + nums[fin])
                return _cache[memo]
            if pl == 2:
                _cache[memo] = min(Solution.Moves(self, nums, ini + 1, fin, 1, _cache) - nums[ini], Solution.Moves(self, nums, ini, fin - 1, 1, _cache) - nums[fin])
                return _cache[memo]

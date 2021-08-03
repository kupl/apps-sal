class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        _dict = {arr[0]: 1}
        res = 1
        for i in arr[1:]:
            if i - difference in _dict:
                _dict[i] = 1 + _dict[i - difference]
                res = max(res, _dict[i])
            else:
                _dict[i] = 1
        return res

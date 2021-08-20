class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            if arr[0] % 2 != 0:
                return 1
        mod = 10 ** 9 + 7
        flag = False
        for i in arr:
            if i % 2 != 0:
                flag = True
                break
        if flag == False:
            return 0
        (even, odd) = (0, 0)
        ret = 0
        for i in arr:
            if i % 2 != 0:
                ret += even + 1
                (odd, even) = (even + 1, odd)
            else:
                ret += odd
                (odd, even) = (odd, even + 1)
        return ret % mod

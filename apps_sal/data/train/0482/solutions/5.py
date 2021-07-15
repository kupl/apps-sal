class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr)>1:
            idx = arr.index(min(arr))
            if 0 < idx < len(arr)-1:
                res += min(arr[idx-1],arr[idx+1]) * arr[idx]
                arr = arr[:idx] + arr[idx+1:]
            elif idx == 0:
                res += arr[1] * arr[idx]
                arr = arr[1:]
            else:
                res += arr[-2] * arr[idx]
                arr = arr[:-1]
        return res
                


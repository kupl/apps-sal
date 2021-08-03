class Solution:
    def helper(self, arr):
        if not arr:
            pass
        else:
            if len(arr) == 1:
                return 0
            else:
                res = sys.maxsize
                max_ind = arr.index(max(arr))
                for div in range(max_ind, max_ind + 2):
                    temp_res = 0
                    if div == 0 or div == len(arr):
                        continue
                    temp_res += max(arr[:div]) * max(arr[div:])
                    temp_res += self.helper(arr[:div])
                    temp_res += self.helper(arr[div:])
                    res = min(res, temp_res)
                    #print (temp_res, div)
                return res

    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.helper(arr)

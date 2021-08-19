class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        sum1 = 0
        mindiff = float('inf')
        val = 0
        n = len(arr)
        for num in arr:
            val = (target - sum1) / n
            if val <= num:
                val = int(val)
                if val + 1 <= num:
                    if abs(target - sum1 - n * val) <= abs(target - sum1 - n * (val + 1)):
                        return val
                    else:
                        return val + 1
                else:
                    return val
            else:
                n -= 1
                sum1 += num
        return arr[-1]

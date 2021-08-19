class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        res = 0
        if len(arr) > 1:
            mr = len(arr) - 1
            while mr - 1 >= 0 and arr[mr - 1] <= arr[mr]:
                mr -= 1
            if mr > 0:
                (cr, res) = (mr, mr)
                prev = -1
                for ml in range(0, len(arr)):
                    if prev <= arr[ml]:
                        while mr < len(arr) and arr[ml] > arr[mr]:
                            mr += 1
                            cr += 1
                        cr -= 1
                        res = min(res, cr)
                    else:
                        break
                    prev = arr[ml]
        return res

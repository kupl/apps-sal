class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        templ = []
        tempr = []
        flag = 0
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i + 1]):
                flag = 1
        if(flag == 0):
            return(0)
        for i in range(1, len(arr)):
            if(arr[i] >= arr[i - 1]):
                templ.append(arr[i - 1])
            else:
                templ.append(arr[i - 1])
                break
        for i in range(len(arr) - 1, 0, -1):
            if(arr[i] < arr[i - 1]):
                tempr.append(arr[i])
                break
            else:
                tempr.append(arr[i])
        print((templ, tempr))
        if(len(templ) == len(tempr)):
            if(len(templ) == len(arr) or len(templ) == 0):
                return(len(templ))
        print((templ, tempr))
        from bisect import bisect_right
        mmax = max(len(templ), len(tempr))
        for i in range(len(tempr)):
            ind = bisect_right(templ, tempr[i])
            print((i, ind))
            mmax = max(mmax, ind + i + 1)
        return(max(0, len(arr) - (mmax)))

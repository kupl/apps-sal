class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        l = len(arr)
        if l == m:
            return l
        
        x = [0 for x in range(l+2)]
        last = -1
        for i in range(l):
            cur = arr[i]
            left, right = x[cur-1], x[cur+1]
            if left == m or right == m:
                last = i
            x
            x[cur-left] = x[cur+right] = left+right+1

        return last

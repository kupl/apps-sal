class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = []
        left = []
        if not arr:
            return 0
        pre = arr[-1] + 1
        while arr and arr[-1] <= pre:
            pre = arr[-1]
            right.append(arr.pop())
        pre = -1
        while arr and arr[0] >= pre:
            pre = arr[0]
            left.append(arr.pop(0))
        l = [i for i in left]
        r = [i for i in right]
        val = 0
        while l and r and l[-1] > r[-1]:
            l.pop()
            val += 1
        out = val
        val = 0
        while right and left and right[-1] < left[-1]:
            right.pop()
            val += 1
        out = min(out, val)
        return out + len(arr)

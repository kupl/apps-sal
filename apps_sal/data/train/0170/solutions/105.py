class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == sorted(arr):
            return 0
        l = [arr[0]]
        r = [arr[-1]]
        for i in range(len(arr)):
            if arr[i + 1] >= arr[i]:
                l.append(arr[i + 1])
            else:
                break
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= arr[i - 1]:
                r.insert(0, arr[i - 1])
            else:
                break
        res1 = len(arr) - len(r)
        res2 = len(arr) - len(l)
        res3 = len(arr)
        if l[-1] <= r[0]:
            res3 = len(arr) - len(l) - len(r)
        res = min(res1, res2, res3)
        j = 0
        for i in range(len(l)):
            while j < len(r) and l[i] > r[j]:
                j += 1
            if j == len(r):
                j -= 1
            p = i
            while p < len(l) and l[p] <= r[j]:
                p += 1
            p -= 1            
            return min(res, len(arr) - (p + 1 + len(r) - j))

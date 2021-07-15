class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrCounter = Counter(arr)
        sortedList = sorted([(key, arrCounter[key]) for key in arrCounter], key = lambda x:(-x[1], x))
        arrLen = len(arr)
        target = arrLen//2
        ans = 0
        for _, aNum in sortedList:
            arrLen -= aNum
            ans += 1
            if arrLen <= target:
                return ans


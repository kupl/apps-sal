class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        stack = [u for u in dic.values()]
        stack.sort()
        L = len(stack)
        ans = 0
        while k > 0:
            test = stack.pop(0)
            if test <= k:
                ans += 1
            k -= test
        return L - ans

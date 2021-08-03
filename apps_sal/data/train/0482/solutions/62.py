class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.mctHelp(arr, 0, len(arr), {})

    def mctHelp(self, arr, a, b, dic):
        if b - a == 1:
            dic[a, b] = 0
        if (a, b) not in dic:
            low = 2**31
            for i in range(a + 1, b):
                res = max(arr[a:i]) * max(arr[i:b]) + self.mctHelp(arr, a, i, dic) + self.mctHelp(arr, i, b, dic)
                low = min(low, res)
            dic[a, b] = low
        return dic[a, b]

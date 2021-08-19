class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i in list(d.keys()):
                d[i] += 1
            else:
                d[i] = 1
        s = len(arr)
        ans = 0
        for j in sorted(list(d.items()), key=lambda x: x[1], reverse=True):
            s -= j[1]
            ans += 1
            if s <= len(arr) // 2:
                return ans
            else:
                continue

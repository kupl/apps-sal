class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        current = {0}
        for x in arr:
            current = {x | y for y in current} | {x}
            ans |= current
        return len(ans)

        if not arr:
            return 0
        l, ans = len(arr), set()
        for i in range(l):
            res = arr[i]
            ans.add(res)
            for j in range(i + 1, l):
                res |= arr[j]
                ans.add(res)
        return len(ans)

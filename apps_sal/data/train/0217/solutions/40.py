class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        current = set()
        current.add(0)
        for i in range(len(arr)):
            a = arr[i]
            s = set()
            s.add(a)
            for y in current:
                s.add(a | y)
            current = s
            ans |= s
        return len(ans)

        # for x in arr:
        #     current = {x | y for y in current} | {x}
        #     # print(current)
        #     ans |= current
        #     # print(ans)
        # return len(ans)

        # brute force time complexity :O(n^2)
        # space complexity:O(n)
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

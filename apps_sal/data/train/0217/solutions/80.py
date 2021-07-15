class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        current = {0}
        for x in arr:
            # print(x,current)
            current = {x | y for y in current} | {x}
            # print(current)
            ans |= current
            # print(ans)
        return len(ans)
    
        # brute force time complexity :O(n^2)
        # space complexity:O(n)
        if not arr:return 0
        l ,ans = len(arr) ,set()
        for i in range(l):
            res = arr[i]
            ans.add(res)
            for j in range(i+1,l):
                res |= arr[j]
                ans.add(res)
        return len(ans)


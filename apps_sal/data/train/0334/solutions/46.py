class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        ans = 0
        r = 0
        ptr = 1
        while ptr < len(cost):
            delete = False
            while ptr < len(cost) and s[ptr] == s[r]:
                # print(ptr,r)
                delete = True
                ptr += 1
            if delete:
                ans += sum(cost[r:ptr]) - max(cost[r:ptr])
                ptr -= 1
            r = ptr
            ptr += 1

        return ans

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        ptr1 = 0
        ptr2 = 0
        ans = 0
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                ptr2 += 1
            else:
                print((ptr1, ptr2))
                if ptr2 > ptr1:
                    ans += sum(cost[ptr1:ptr2+1]) - max(cost[ptr1:ptr2+1])
                ptr1, ptr2 = i, i
        if ptr2 > ptr1:
            ans += sum(cost[ptr1:ptr2+1]) - max(cost[ptr1:ptr2+1])
        return ans
                


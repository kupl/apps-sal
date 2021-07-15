class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre = 0
        sums = [0]
        for el in nums:
            pre += el
            sums.append(pre)
            
        #print(\"---\")
       # print(sums)
        ans = 0
        seen = {} # seen[v] = i iff sums[i] == v
        for i, v in enumerate(sums):
            #print(f\"seen: {seen}\")
            if v-target in seen:
                ans += 1
                seen = {} # satisfies non-overlapping
            seen[v] = i
        #print(f\"seen: {seen}\")
        return ans
            


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left,right=-1,0
        seen = Counter()
        ans = 0
        while left<=right<len(tree):
            while right<len(tree) and (len(seen) < 2 or tree[right]in seen):
                seen[tree[right]]+=1
                right+=1
                
            ans = max(ans,right-left-1) #-1?

            left+=1
            seen[tree[left]]-=1
            if seen[tree[left]]==0:
                del seen[tree[left]]
                
        return ans

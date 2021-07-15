class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxL = 0
        l, r = 0, 0 # 0, 4
        if len(set(tree)) < 3:
            return len(tree)
        
        while r <= len(tree):
            temp = tree[l:r]
            if len(set(temp)) < 3:
                maxL = max(maxL, len(temp))
                r += 1
            elif len(set(temp)) >= 3:
                l += 1
        
        return maxL

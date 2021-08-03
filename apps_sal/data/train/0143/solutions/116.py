class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if(len(tree) == 1):
            return 1
        if(not tree):
            return 0
        i = 0
        j = 1
        l = len(tree)
        ans = 0
        found = False
        second = tree[1]
        count = 1
        while(i < l and j < l):
            if(tree[i] != tree[j] and not found):
                second = tree[j]
                found = True
            if(found and tree[j] != second and tree[j] != tree[i]):
                ans = max(ans, count)
                count = 0
                i += 1
                j = i
                found = False
            j += 1
            count += 1
        ans = max(ans, count)
        return ans

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        l = 0
        mp = collections.defaultdict(int)
        fruits = 1
        for i in range(0, len(tree)):
            mp[tree[i]] += 1
            while len(mp) > 2:
                mp[tree[l]] -= 1
                if mp[tree[l]] == 0:
                    del mp[tree[l]]
                l += 1
            fruits = max(fruits, i-l+1)
        return fruits
            
                
                


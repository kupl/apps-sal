class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        j = 0
        my_map = {}
        max_len = 0
        while i < len(tree):
            while i < len(tree) and (tree[i] not in my_map and len(my_map) < 2 or tree[i] in my_map):
                if tree[i] not in my_map:
                    my_map[tree[i]] = 0
                my_map[tree[i]] += 1
                i += 1
            max_len = max(max_len, i - j)
            while len(my_map) == 2: 
                my_map[tree[j]] -= 1
                if my_map[tree[j]] == 0:
                    del my_map[tree[j]]
                j += 1
            
        return max_len


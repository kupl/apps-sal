class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        
        if n < 3:
            return n
        
        max_count = 0

        set_1 = {tree[0]}
        count_1 = 1
        set_2 = set_1.copy()
        count_2 = 1
        
        
        for i in range(1, n):
            if tree[i] in set_2:
                count_2 += 1
            else:
                temp = set_1.copy()
                temp.add(tree[i])
                set_2 = temp
                count_2 = count_1 + 1
            if tree[i] in set_1:
                count_1 += 1
            else:
                set_1 = {tree[i]}
                count_1 = 1
                
            max_count = max(max_count, max(count_1, count_2))
            
            
        return max_count
                


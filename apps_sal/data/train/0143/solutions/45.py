from collections import Counter

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        num_fruit = Counter()
        j, num_type, max_fruit = 0, 0, 0
        for i in range( len(tree) ):
            if num_fruit[ tree[i] ] == 0: num_type += 1
            num_fruit[ tree[i] ] += 1
            
            if num_type <= 2:
                max_fruit = max( i-j+1, max_fruit )
            else:
                while True:
                    num_fruit[ tree[j] ] -= 1
                    j += 1
                    if num_fruit[ tree[j-1] ] == 0: break
                num_type -= 1
        
        return max_fruit

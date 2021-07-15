class Solution:
    def total(self, fruits):
        total = 0
        for key in fruits:
            total += fruits[key]
        
        return total
    
    def totalFruit(self, tree: List[int]) -> int:
        
        fruits = {}
        left_index = 0
        best = 0
        
        for right_index in range(len(tree)):
            curr_fruit = tree[right_index]
            
            if curr_fruit not in fruits:
                fruits[curr_fruit] = 1
            else:
                fruits[curr_fruit] += 1
            
            while len(fruits) > 2:
                old_fruit = tree[left_index]
                fruits[old_fruit] -= 1
                if fruits[old_fruit] == 0:
                    del fruits[old_fruit]
                left_index += 1 
                
            best = max(best, self.total(fruits))
        
        return best
            


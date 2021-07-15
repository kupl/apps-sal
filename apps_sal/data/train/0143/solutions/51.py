class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        maxi = 0
        
        for fruit in tree:
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max+=1
            else:
                current_max = last_fruit_count + 1
                
            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count = 1
                
            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit
                
            
            maxi = max(current_max, maxi)
            
        return maxi

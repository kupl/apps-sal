class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        #You want a basket that can get both. 
        total_fruits = collections.defaultdict(int)
        unique_baskets = 0
        max_fruit_types = 0 
        start = 0
        for end in range(len(tree)):
            cur_fruit = tree[end]
            total_fruits[cur_fruit] += 1 
            if total_fruits[cur_fruit] == 1: #then we know there is a unique fruit here
                unique_baskets += 1 
                
            while unique_baskets >= 3: 
                start_fruit = tree[start]
                total_fruits[start_fruit] -= 1
                if not total_fruits: #this means that we have less unique baskets now 
                    unique_baskets -= 1 
                start += 1
                    
            max_fruit_types = max(max_fruit_types, end - start + 1)
            
        return max_fruit_types
            
#         #Start at ANY tree of my choice 
#         #Then perform the steps 
# #         1) Add one fruit from the tree to basket. If you can't you stp 
# #         2) Move to the next tree to the RIGHT of the current tree if there is no such tree you stop. 
        
#     #So you reset back to step 1 after you're done. 
#     #So this means that once you're done and because we want to GET all possible fruits through your positions 
# #         WANT: Total amount of fruit collected 
#         last_fruit = -1 
#         second_last_fruit = -1 
#         last_fruit_count = 0
#         total_fruits = 0 
#         cur_fruits_max = 0 
#         #Let's call prev fruits 
#         #last_fruit, second_last_fruit 
#         # fruit is our CURRENT fruit 
        
#         #So we have 2 prev fruit and current fruit.  
#         #If fruit is the second_last_fruit 
#         #We will know 
#         for fruit in tree: 
#             if fruit == last_fruit or fruit == second_last_fruit: 
#                 cur_fruits_max += 1 
                
#             else: 
#                 cur_fruits_max = last_fruit_count + 1 #this means we picked you new fruit 
                
     
#             #You need to check fruit with last fruit not second to last fruit since last fruit will be your \"best case scenario\"
#             if fruit == last_fruit: 
#                 last_fruit_count += 1 
#             else: 
#                 last_fruit_count = 1 #never been seen before (base case)
            
#             #This means that we'd be double counting if we moved you beforehand 
#             if fruit != last_fruit: #meaning your a second_last_fruit basically 
#                 second_last_fruit = last_fruit 
#                 last_fruit = fruit 
                
#             total_fruits = max(total_fruits, cur_fruits_max)
            
#         print(total_fruits)
#         # (O(N)) run time 
#         return total_fruits 
class Solution():
    def totalFruit(self, tree):
        fruit_basket = collections.defaultdict(int)
        unique_fruits = 0 
        total_fruits = 0 
        start = 0
        end = 0 
        for end in range(len(tree)): 
            type_of_fruit = tree[end]
            fruit_basket[type_of_fruit] += 1 #Defaultdict so if not there instantiate it and add one 
            #small check to count it one time for the fruit 
            if fruit_basket[type_of_fruit] == 1: 
                unique_fruits += 1 
                
            while unique_fruits > 2:
                start_fruit = tree[start]
                fruit_basket[start_fruit] -= 1 
                if not fruit_basket[start_fruit]: #meaning it's empty 
                    unique_fruits -= 1 
                start += 1 
            total_fruits = max(total_fruits, end - start + 1)
        return total_fruits
        
#Map Way   
# import collections
# class Solution():
#     def totalFruit(self, tree):
#         count = collections.defaultdict(int)
#         unique = res = end = start = 0
#         while end < len(tree):
#             count[tree[end]] += 1
#             if count[tree[end]] == 1: unique+=1
#             while unique > 2:
#                 count[tree[start]] -= 1
#                 if not count[tree[start]]: 
#                     unique -= 1
#                 start += 1
#             res = max(res, end - start + 1)
#             end += 1
#         return res
            
                
        
        
        
            
            
            




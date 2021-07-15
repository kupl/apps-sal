class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        best_so_far = start = 0
        fruit_1 = fruit_2 = fruit_1_last_index = fruit_2_last_index = None
        
        for end in range(len(tree)):
            # If we haven't picked any fruit yet, put this fruit in basket 1
            if fruit_1 is None:
                fruit_1 = tree[end]
                fruit_1_last_index = end
                
            # If we haven't picked two different fruits yet, put this fruit in backet 2
            elif fruit_2 is None and tree[end] != fruit_1:
                fruit_2 = tree[end]
                fruit_2_last_index = end
                
            # We have picked at least 2 different fruits so far
            else:
                # If this is basket 1's fruit, remember this as the most recent place we saw fruit 1
                if tree[end] == fruit_1:
                    fruit_1_last_index = end
                    
                # If this is basket 2's fruit, remember this as the most recent place we saw fruit 2
                elif tree[end] == fruit_2:
                    fruit_2_last_index = end
                    
                # This is neither fruit 1 nor fruit 2
                else:
                    # This is as far as we can go with these two fruits. Remember how many fruits we got.
                    best_so_far = max(best_so_far, end - start)
                    
                    # Replace <the fruit whose most recent sighting was longer ago> with this new fruit
                    if fruit_1_last_index < fruit_2_last_index:
                        start = fruit_1_last_index + 1
                        fruit_1 = tree[end]
                        fruit_1_last_index = end
                    else:
                        start = fruit_2_last_index + 1
                        fruit_2 = tree[end]
                        fruit_2_last_index = end
        
        return max(best_so_far, len(tree) - start)

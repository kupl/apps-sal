class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        if len(set(tree)) <= 2:
            return len(tree)
        
        max_collected = 0
        
        for i in range(len(tree)):
            num_collected = 0
            different_types = set()
            for j in range(i, len(tree)):
                if len(different_types) < 2:
                    different_types.add(tree[j])
                    num_collected += 1
                elif tree[j] in different_types:
                    num_collected += 1
                else:
                    break
            
            max_collected = max(max_collected, num_collected)
        
        return max_collected

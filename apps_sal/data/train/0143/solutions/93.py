class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        char_to_count = defaultdict(int)
        unique_chars = 0
        
        start = 0
        end = 0
        max_fruit = 0
        while end < len(tree):
            char_to_count[tree[end]] += 1
            if char_to_count[tree[end]] == 1:
                unique_chars +=  1
            
            while unique_chars > 2:
                char_to_count[tree[start]] -= 1
                if char_to_count[tree[start]] == 0:
                    unique_chars -= 1
                start += 1
            end += 1
            max_fruit = max(max_fruit, end-start)
            
        return max_fruit


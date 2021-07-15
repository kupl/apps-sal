class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxStreak = 0
        i = 0
        types = set()
        last_type = 0
        streak = 0
        while i < len(tree):
            if len(types) == 0 or len(types) == 1:
                types.add(tree[i])
                last_type = i
                streak += 1
                i += 1
            else:
                if tree[i] in types:
                    if tree[last_type] != tree[i]:
                        last_type = i
                    streak += 1
                    i += 1
                else:
                    i = last_type
                    types = set()
                    maxStreak = max(streak, maxStreak)
                    streak = 0
                    
        return max(streak, maxStreak)


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        combinations = [set()]
        
        for a in arr:
            chars = set(a)
        
            if len(chars) != len(a):
                continue
            
            for c in combinations:
                if len(chars.intersection(c)) == 0:
                    combinations.append(chars.union(c))
            
        return max([len(c) for c in combinations])


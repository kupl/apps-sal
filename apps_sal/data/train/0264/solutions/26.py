class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def isUniqueChars(s):
            return len(set(s)) == len(s)
        
        
        # Get filter out bad input.
        arr = [set(w) for w in arr if isUniqueChars(w)]
        results = list(arr)
        
        for w in arr:
            temp = []
            for r in results:
                if not w.intersection(r):
                    temp.append(w.union(r))
            results = results + temp
            
        max_length = 0
        for w in results:
            max_length = max(max_length, len(w))
                
        return max_length        

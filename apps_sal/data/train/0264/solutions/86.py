class Solution:
    def maxLength(self, arr: List[str]) -> int:
        d = {}
        def helper(banned,start):
            if start == len(arr):
                return len(banned)
            k = tuple(sorted(str(banned)+str(start)))
            if k in d:
                return d[k]
            string = arr[start]
            new_set = set()
            for i in string:
                if i in banned or i in new_set:
                    return helper(banned,start+1)
                new_set.add(i)
            new_banned = banned.union(new_set)
            val = max(helper(new_banned,start+1),helper(banned,start+1))
            d[k] = val
            return val
        initial_banned = set()
        res = helper(initial_banned,0)
        return res
        
        
            
            


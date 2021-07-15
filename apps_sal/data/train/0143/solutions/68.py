class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counter = collections.defaultdict(int)
        
        start = 0
        res = 0
        
        for end in range(len(tree)):
            counter[tree[end]] += 1
            
            while len(list(counter.keys())) > 2:
                counter[tree[start]] -= 1
                
                if counter[tree[start]] == 0:
                    del counter[tree[start]]
                
                start += 1
            res = max(res, sum(counter.values()))
        
        return res
            
            
                


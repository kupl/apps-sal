class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        d =defaultdict(list)
        n = len(labels)
        for i in range(n):
            d[labels[i]].append(values[i])
        
        arr = []
        for k,v in list(d.items()):
            d[k].sort(reverse=True)
            d[k] = d[k][:use_limit]
            arr.extend(d[k])
        
        arr.sort(reverse=True)
        return sum(arr[:num_wanted])
        
        
            


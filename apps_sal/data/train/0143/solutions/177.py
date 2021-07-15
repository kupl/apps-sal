class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxCount = count = 0
        head = back = 0
        buckets = dict()
        while back < len(tree):
            fruit = tree[back]
            if fruit in buckets:
                buckets[fruit] += 1  
            else:
                buckets[fruit] = 1
                while len(list(buckets.keys())) > 2:
                    dropFruit = tree[head]
                    buckets[dropFruit] -= 1
                    if buckets[dropFruit] == 0:
                        buckets.pop(dropFruit)
                    count -= 1
                    head += 1
            count += 1
            maxCount = max(maxCount, count)
            back += 1
        return maxCount
                
                    
                    
            


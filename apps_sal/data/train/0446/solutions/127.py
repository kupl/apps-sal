class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        count = 0
        for i in sorted(list(c.items()), key = lambda x: x[1]):
            # print(i)
            if k - i[1] >= 0:
                k -= i[1]
                count += 1
            elif k - i[1] < 0:
                break
        return len(c)-count
        
            
        


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        

        dict = {}
        for num in arr:
            dict[num] = dict.get(num,0) + 1
            
            
            
        size = len(arr) + 1
        buckets = [[] for _ in range(size)]
        
                
        for num, freqency in list(dict.items()):
            buckets[freqency].append(num)
            
            
        for i in range(size):
            if k == 0: 
                break
                
            while buckets[i] and k >= i:
                num = buckets[i].pop()
                del dict[num]
                k -= i
        return len(dict)
    
    
#         buckets = [[] for _ in range(len(arr) + 1)]
#         counter = collections.Counter(arr)
#         for key, count in counter.items():
#             buckets[count].append(key)
#         for count in range(len(arr) + 1):
#             if k == 0: break
#             while buckets[count] and k >= count:
#                 del counter[buckets[count].pop()]
#                 k -= count
#         return len(counter)


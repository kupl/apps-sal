class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for i in arr:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        
        values = []
        frequencies = []
        for key in freq.keys():
            values.append(key)
            frequencies.append(freq[key])
        
        frequencies = sorted(frequencies)
        distinct = len(frequencies)
        ind = 0
        for i in range(distinct):
            k -= frequencies[i]
            if (k < 0):
                return distinct-i
            elif (k == 0):
                return distinct-i-1
            i += 1
            
        return 0

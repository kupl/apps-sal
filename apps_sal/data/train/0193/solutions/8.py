class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        L = len(arr)
        
        count = collections.Counter(arr)
        freq = sorted(count.values())
        size = 0
        res = 0
        
        for i in range(len(freq)-1, -1, -1):
            size += freq[i]
            res += 1
            if size >= L/2:
                return res

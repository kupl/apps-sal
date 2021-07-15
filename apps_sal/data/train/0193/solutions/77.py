class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        n = len(arr)
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        num_freq = list(sorted([v for k,v in d.items()]))
        tot = 0
        m = len(num_freq)
        i = 0
        
        while(tot < n/2 and i<m):
            tot += num_freq[m-i-1]
            i+=1
            print(i)
        print(num_freq)
        return i

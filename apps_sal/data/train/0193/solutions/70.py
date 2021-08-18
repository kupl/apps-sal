class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        n = len(arr)
        arr_map = Counter(arr)
        arr_tup = [(item, arr_map[item]) for item in arr_map]
        arr_tup = sorted(arr_tup, key=lambda x: -x[1])
        count = 0
        total = 0
        for item in arr_tup:
            total += item[1]
            print((item[0]))
            count += 1
            if total >= n / 2:
                return count

    ''' n = len(arr)
        
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        new_set = set()
                
        max_freq = max(freq, key = freq.get)
        del(freq[max_freq])
        
        new_set.add(max_freq)
        
        arr = [val for val in arr if val != max_freq]
        
        while True:
            
            if len(arr) <= n//2:
                return len(new_set)
            else:
                max_freq = max(freq, key = freq.get)
                del(freq[max_freq])
                new_set.add(max_freq)
                arr = [val for val in arr if val != max_freq]'''

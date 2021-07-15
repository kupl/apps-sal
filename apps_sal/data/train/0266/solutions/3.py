class Solution:
    def numSplits(self, s: str) -> int:
        def decorate(a, b):
            final = {1: defaultdict(int), 2 : defaultdict(int)}
            count1, count2 = 0, 0
            for char in a:
                final[1][char] += 1
                if final[1][char] == 1: count1 += 1
                
            for char in b:
                final[2][char] += 1
                if final[2][char] == 1: count2 += 1
            return final, count1, count2
            
        split = None
        count1, count2 = 0, 0
        total = 0
        for point in range(1, len(s)):
            if split == None:
                split, count1, count2 = decorate(s[:point], s[point:])
            else:
                split[1][s[point-1]] += 1
                if split[1][s[point-1]] == 1: count1 += 1
                
                split[2][s[point-1]] -= 1
                if split[2][s[point-1]] == 0: count2 -= 1
            
            # print(s[:point], s[point:], count1, count2)
            if count1 == count2: total += 1
        
        return total


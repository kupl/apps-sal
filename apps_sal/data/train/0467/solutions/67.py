class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divs = dict()
        
        for v in nums:
            divs.setdefault(v, [0, []])
            divs[v][0] += 1
        
        n = max(nums)
        sieve = (1 + n) * [0]
            
        for i in range(2, 1 + n):
            j = i
                
            while j <= n:
                sieve[j] += 1
                    
                if j in divs:
                    divs[j][1].append(i)
                    
                j += i
            
        # print(divs)
            
        return sum([freq * (1 + sum(cur_div)) for k, (freq, cur_div) in list(divs.items()) if len(cur_div) == 3])


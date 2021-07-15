class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = {}
        
        def iseven(n):
            return n%2==0
        
        ans = 0
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        keys = list(count.keys())
        for n in keys:
            if n == 0:
                count.pop(n)
            if not iseven(n):
                ans += count[n]
                n -= 1                
                if n != 0:
                    count[n] = count.get(n,0) + count[n+1]
                count.pop(n+1)
            
        while len(count) > 0:
            # print(ans)
            # print(count)
            keys = list(count.keys())
            ans += 1
            new_count = {}
            for n in keys:
                if not iseven(int(n/2)):
                    if int(n/2) != 1:
                        new_count[int(n/2)-1] = new_count.get(int(n/2)-1, 0) + count[n]
                    ans += count[n]
                else:
                    new_count[int(n/2)] = new_count.get(int(n/2), 0) + count[n]
                    
            count = new_count
            
        return ans
                
            


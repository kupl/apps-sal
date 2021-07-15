class Solution:
    def numSub(self, s: str) -> int:
        # 10/6/20
        dic = collections.defaultdict(int)
        
        n = len(s)
        left, right = 0, 0
        while left < n:
            if s[left] == '1':
                right = left
                while right < n and s[right] == '1':
                    right += 1
                dic[right-left] += 1
                left = right
            else:
                left += 1
        
        total = 0
        for ones in dic:
            total = (total + (ones *(ones+1)) // 2 * dic[ones]) % (10**9 + 7)
        return total
            
        
        
        


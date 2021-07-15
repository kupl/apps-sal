class Solution:
    def minDays(self, n: int) -> int:
        
        q = {n}
        seen = set()
        ans = 1
        while q:
            q2 = set()
            for num in q:
                if num == 1:
                    return ans
                seen.add(num)
                q2.add(num-1)
                if num%2 == 0:
                    q2.add(num//2)
                if num%3 == 0:
                    q2.add(num//3)
            q = q2
            ans += 1
        


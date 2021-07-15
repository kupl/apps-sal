class Solution:
    def minDays(self, n: int) -> int:
        self.ans = float('inf')
        @lru_cache(None)
        def search(days,num):
            if num==0:
                if days<self.ans:
                    self.ans = days
                return
            if days+int(math.log(num)/math.log(3))+1>=self.ans:
                return
            days += 1
            if not num%3:
                search(days,num//3)
            if not num%2:
                search(days,num//2)
            search(days,num-1)
            return
        
        search(0,n)
        return self.ans

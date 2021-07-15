class Solution:
    def getProbability(self, balls: List[int]) -> float:
        from math import factorial as f
        n = len(balls)
        first = [0]*n
        second = [0]*n
        self.ans = 0
        def dfs(i):
            if i == n:
                if sum(first) != sum(second):
                    return 
                if len([x for x in first if x != 0]) != len([x for x in second if x != 0]):
                    return
                
                ret = f(sum(first)) * f(sum(second))
                for num in first:
                    if num != 0:
                        ret /= f(num)
                for num in second:
                    if num != 0:
                        ret /= f(num)
                self.ans += ret
                return
                
                
            else:
                for num in range(0, balls[i]+1):
                    first[i] = num
                    second[i] = balls[i]-num
                    dfs(i+1)
        dfs(0)
        
        total = f(sum(balls))
        for num in balls:
            total /= f(num)
        return self.ans/total
                
        


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        M = len(balls)
        N = sum(balls)
        F = [math.factorial(n) for n in range(N // 2 + 1)]
        # every box has at least N // 2 distinct colors, and has at most N distinct colors
        
        s1 = [0] * M
        s2 = [0] * M
        
        def find(i):
            if i == M:
                if sum(s1) == sum(s2) and len([n for n in s1 if n]) == len([n for n in s2 if n]):
                    # print(s1, s2)
                    base1 = F[N // 2]
                    for n in s1:
                        base1 //= F[n]
                    base2 = F[N // 2]
                    for n in s2:
                        base2 //= F[n]
                    self.ans += base1 * base2
                return
            
            for n in range(balls[i]+1):
                s1[i] = n
                s2[i] = balls[i] - n
                find(i+1)
                
        self.ans = 0
        find(0)
        
        base = math.factorial(N)
        for n in balls:
            base //= math.factorial(n)
        
        return self.ans / base

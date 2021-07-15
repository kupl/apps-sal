class Solution:
    def getProbability(self, balls: List[int]) -> float:
        from scipy.special import comb # help to calculate combination numbers
        
        sm = sum(balls)
        number_of_combinations = comb(sm, sm//2) # 
        
        def number_of_ways_to_pick(n): # there are n balls of color-a, we want to pick some number of them and put them into boxA, and others into boxB
            d = Counter() # key: number of balls put into boxA, value: number of such combinations
            for i in range(n+1):
                d[i] = comb(n,i)
            return d
            
        status = Counter()
        status[(0,0,0,0)] = 1 
        #key: num of balls in boxA, num of balls in boxB, different colors in boxA, different colors in boxB; value: number of such combinations
        for n in balls:
            combs = number_of_ways_to_pick(n)
            new_s = Counter()
            for k in status:
                a,b,ca,cb = k
                for n_a in combs:
                    if n_a == 0:
                        new_s[(a,b+n,ca,cb+1)] += status[k] * combs[n_a]
                    elif n_a == n:
                        new_s[(a+n,b,ca+1,cb)] += status[k] * combs[n_a]
                    else:
                        new_s[(a+n_a, b+n-n_a, ca, cb)] += status[k] * combs[n_a]
            status = new_s
        
        res = 0
        for k in status:
            a,b,ca,cb = k
            if a==b and ca==cb:
                res += status[k]
            
        return res/number_of_combinations


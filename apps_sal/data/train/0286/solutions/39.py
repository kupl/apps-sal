class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k, n = len(balls), sum(balls)
        
        total = 2 * math.comb(n, n//2)
        def shuffle(color, box1, box2):
            if color == k:
                if sum(box1) == sum(box2) and  box1.count(0) == box2.count(0):
                    #print(f'{box1} {box2}')
                    ans = 0
                    for box in [box1, box2]:
                        p = 1
                        for c, num in enumerate(box):
                            p *= math.comb(balls[c], num)
                        ans += p
                    return ans
                else:
                    return 0
            # track all possible
            total_p = 0
            bc = balls[color]
            for b in range(0, bc + 1):
                box1[color], box2[color] = b, bc - b
                total_p += shuffle(color + 1, box1, box2)
                box1[color], box2[color] = 0, 0
            return total_p
                
        p = shuffle(0, [ 0 ] * k, [ 0 ] * k)
        return p / total
                
            
            
                


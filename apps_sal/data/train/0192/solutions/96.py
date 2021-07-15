class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        d = [0] * 10 ** 4
        t = 0
        total = 0

        for p in piles:
            d[p - 1] += 1
            
        for i in range(len(d)):
            while d[i] > 0:
                d[i] -= 1
                if t >= len(piles) // 3 and t % 2 == ((len(piles) // 3) % 2):
                    total += i + 1
                t += 1


        
        return total        

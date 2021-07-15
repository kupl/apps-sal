class Solution:
    def isPossibleDivide(self, hand : List[int], W: int) -> bool:
        
        if len(hand) % W != 0:
            return False
        
        hand.sort()
        cnt = collections.Counter(hand)
        
        for n in hand:
            if cnt[n] > 0:
                t = 0
                while t < W:
                    cnt[n + t] -= 1
                    if cnt[n + t] < 0:
                        return False
                    t += 1
        return True
                


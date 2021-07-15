class Solution:
    def isPossibleDivide(self, hand: List[int], W: int) -> bool:
        
        l = len(hand)
        if l == 0 or l % W != 0:
            return False
        
        counter = collections.Counter(hand)
        heapq.heapify(hand)
        
        pos = 0
        while pos < l:
            while not hand[0] in counter:
                heapq.heappop(hand)
            
            currMin = hand[0]
            counter[currMin] -= 1
            pos += 1
            if counter[currMin] == 0:
                del counter[currMin]
            
            for i in range(W-1):
                nextDraw = currMin + i + 1
                if nextDraw in counter and counter[nextDraw] > 0:
                    counter[nextDraw] -= 1
                    pos += 1
                    if counter[nextDraw] == 0:
                        del counter[nextDraw]
                else:
                    return False
                
        return True
                
                    
            


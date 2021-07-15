from queue import Queue
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        q = Queue()
        mem = dict()

        q.put((0, 0))

        while not q.empty():
            curr = q.get()
            
            for c in coins:
                tot = curr[1] + c
                if tot > amount:
                    continue
                if tot == amount:
                    return curr[0] + 1

                if tot in mem and mem[tot] <= curr[0] + 1:
                    continue
                
                q.put((curr[0] + 1, tot))
                mem[tot] = curr[0] + 1

        return -1

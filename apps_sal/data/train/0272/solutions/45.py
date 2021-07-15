import queue

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        q = queue.Queue()
        notopen = set()
        op = set()
        for x in initialBoxes:
            q.put(x)
        
        while not q.empty():
            # print(q.queue)
            cur = q.get()
            if status[cur] == 1:
                ans += candies[cur]
                for k in keys[cur]:
                    status[k] = 1
                    if k in notopen and k not in op:
                        q.put(k)
                        op.add(k)
                for c in containedBoxes[cur]:
                    q.put(c)
            else:
                notopen.add(cur)
        
        return ans


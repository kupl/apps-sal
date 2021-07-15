from queue import Queue
class Solution:
    def minDays(self, n: int) -> int:
        q = Queue()
        q.put(n)
        vis = set()
        vis.add(n)
        ans = 1
        while True:
            sz = q.qsize()
            for rep in range(sz):
                u = q.get()
                if u == 1:
                    return ans
                if u - 1 not in vis:
                    vis.add(u - 1)
                    q.put(u - 1)
                if u % 2 == 0 and u // 2 not in vis:
                    vis.add(u // 2)
                    q.put(u // 2)
                if u % 3 == 0 and u // 3 not in vis:
                    vis.add(u // 3)
                    q.put(u // 3)
            ans += 1
        return -1

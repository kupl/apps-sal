import queue


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        temp = {}
        for n in arr:
            if n not in temp:
                temp[n] = 0
            temp[n] += 1
        q = queue.PriorityQueue()
        for (n, c) in temp.items():
            q.put((c, n))
        while k > 0:
            (c, n) = q.get()
            if k < c:
                q.put((c, c - k))
                break
            k -= c
        return len(q.queue)

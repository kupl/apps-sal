import queue


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for i in arr:
            if counter.__contains__(i):
                counter[i] += 1
            else:
                counter[i] = 1
        q = queue.PriorityQueue()
        for i in counter:
            q.put((counter[i], i))
        lastCutted = True
        while k > 0:
            element = q.get()
            count = element[0]
            if k >= count:
                lastCutted = True
            else:
                lastCutted = False
            k -= count
        if lastCutted:
            return q.qsize()
        else:
            return q.qsize() + 1

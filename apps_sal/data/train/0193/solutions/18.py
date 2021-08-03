'''
Keep a dict of counts and add all of them to a heap. Then we remove from heap until size <= half and we return size of set that we have to remove
'''
from heapq import heapify, heappush, heappop


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        maxheap = []
        for i, freq in list(counts.items()):
            maxheap.append((-freq, i))
        heapify(maxheap)
        curN = len(arr)
        sol = 0
        while curN > len(arr) / 2:
            freq, cur = heappop(maxheap)
            curN += freq
            sol += 1

        return sol

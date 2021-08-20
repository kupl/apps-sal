from typing import List
from heapq import *


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = {}

        def insert(num):
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in arr:
            insert(num)
        valkeys = [(hashmap[key], key) for key in list(hashmap.keys())]
        kSmallest = nsmallest(k, valkeys)
        uniqueCount = len(valkeys)
        removals = k
        for (occ, num) in kSmallest:
            if removals - occ >= 0:
                removals -= occ
                uniqueCount -= 1
            else:
                break
        return uniqueCount

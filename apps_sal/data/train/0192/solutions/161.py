class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        def mergeSort(l):
            if len(l) < 2:
                return l
            pivot = l[0]
            return mergeSort([x for x in l if x > pivot]) + [x for x in l if x == pivot] + mergeSort([x for x in l if x < pivot])

        sortedPiles = mergeSort(piles)
        sumlimit = (2 * len(piles)) // 3
        sumind = list(range(1, sumlimit, 2))
        return sum([sortedPiles[i] for i in sumind])

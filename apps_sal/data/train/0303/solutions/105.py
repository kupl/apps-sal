class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        hashmap = {}

        def partitionMatrix(lst, currScore):
            key = tuple(lst)
            if key in hashmap:
                return hashmap[key] + currScore
            if lst == []:
                hashmap[key] = 0
                return currScore
            for i in range(1, k + 1):
                if len(lst) == i:
                    hashmap[key] = (max(lst) * i)
                    return currScore + (max(lst) * i)
            best = currScore
            for i in range(1, k + 1):
                subScore = max(lst[:i]) * i
                best = max(best, partitionMatrix(lst[i:], currScore + subScore))
            hashmap[key] = best - currScore
            return best
        return partitionMatrix(arr, 0)

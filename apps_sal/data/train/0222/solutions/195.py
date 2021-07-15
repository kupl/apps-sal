class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibSeqs = {}
        values = set(arr)

        for i in range(len(arr)):
            for j in range(i-1, -1, -1):
                a = arr[i] - arr[j]
                if a >= arr[j]:
                    break
                if a in values:
                    fibSeqs[arr[j], arr[i]] = fibSeqs.get((a, arr[j]), 2) + 1

        return max(fibSeqs.values() or [0])

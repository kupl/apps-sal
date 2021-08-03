class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return self.recur(arr, len(arr) - 1, k, {})

    def recur(self, arr, index, k, hashMap):
        if index < 0:
            return 0

        if index in hashMap:
            return hashMap[index]
        result = 0
        maxV = 0
        for i in range(k):
            if index - i < 0:
                continue
            maxV = max(maxV, arr[index - i])
            result = max(result, maxV * (i + 1) + self.recur(arr, index - i - 1, k, hashMap))

        hashMap[index] = result
        return result

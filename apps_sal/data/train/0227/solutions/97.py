class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        hashMap = {}
        windowStart = 0
        m = 0
        hashMap[1] = 0
        for windowEnd in range(len(A)):
            if A[windowEnd] not in hashMap:
                hashMap[A[windowEnd]] = 0
            hashMap[A[windowEnd]] += 1
            while sum(hashMap.values()) - hashMap[1] > K:
                hashMap[A[windowStart]] -= 1
                windowStart += 1
            m = max(m, windowEnd - windowStart + 1)
        return m

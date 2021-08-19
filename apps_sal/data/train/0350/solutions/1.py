class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K > len(A):
            return 0
        result = checker = windowStart = 0
        hashMap = {}
        a_length = len(A)
        for windowEnd in range(a_length):
            curr_str = A[windowEnd]
            if curr_str in hashMap:
                hashMap[curr_str] += 1
            else:
                hashMap[curr_str] = 1
            if len(hashMap) > K:
                del hashMap[A[checker]]
                checker += 1
                windowStart = checker
            if len(hashMap) == K:
                while hashMap[A[checker]] > 1:
                    hashMap[A[checker]] -= 1
                    checker += 1
                result += checker - windowStart + 1
        return result

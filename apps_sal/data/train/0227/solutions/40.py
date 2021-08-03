class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        maxlength = 0
        hashmap = {}
        count = 0
        while right < len(A):
            hashmap[A[right]] = hashmap.get(A[right], 0) + 1
            while A[right] == 0 and hashmap[A[right]] > K:
                hashmap[A[left]] -= 1
                left += 1
            maxlength = max(maxlength, right - left + 1)
            right += 1
        return maxlength

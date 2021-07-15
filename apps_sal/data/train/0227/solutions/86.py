class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        k = 0
        flipped = set()
        longest = 0
        while right < len(A):
            if A[right] == 1:
                longest = max(longest, right - left + 1)
                right += 1
            elif A[right] == 0 and k < K:
                flipped.add(right)
                longest = max(longest, right - left + 1)
                right += 1
                k += 1
            elif left == right:
                right += 1
                left += 1
            else:
                if left in flipped:
                    flipped.discard(left)
                    k -= 1
                left += 1
            
            
        return longest

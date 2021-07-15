class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left = [i+a for i,a in enumerate(A)]
        right = [b-j for j, b in enumerate(A)]
        for i in range(1, len(left)):
            left[i] = max(left[i], left[i-1])
        for i in range(len(right)-1)[::-1]:
            right[i] = max(right[i], right[i+1])
        return max(l+r for l, r in zip(left[:-1], right[1:]))


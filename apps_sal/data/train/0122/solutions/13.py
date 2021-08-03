class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k or n < k:
            return total
        remove = n - k
        ans = 0

        '''memo = [0]*(n+1)
        memo[0] = 0
        
        start = 0
        for i in range(0, n):
            memo[i+1] = memo[i] + cardPoints[i]            
            if i-start + 1 == remove: 
                ans = max(ans, total-(memo[i+1]-memo[start]))
                start = start+1'''
        curr = 0
        start = 0
        for right in range(n):
            curr += cardPoints[right]
            if right - start + 1 == remove:
                ans = max(ans, total - curr)
                curr -= cardPoints[start]
                start += 1

        return ans

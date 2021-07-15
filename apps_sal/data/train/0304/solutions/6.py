class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        
        freq = Counter(ages)
        
        def can_request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
            
        ans = 0
        for a1 in range(1, 121):
            for a2 in range(1, 121):
                if can_request(a1, a2):
                    ans += (freq[a1] * freq[a2]) if a1 != a2 else (freq[a1] * (freq[a1]-1))     
        return ans

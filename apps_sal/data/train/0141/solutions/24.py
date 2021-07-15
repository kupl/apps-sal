class Solution:
    def numRescueBoats(self, people: List[int], cap: int) -> int:
        people.sort()
        N = len(people)
        i, j = 0, N - 1
        
        ans = 0
        k = cap
        s = 2
        
        while i <= j:
            # prioritize heavier one
            while s and j >= 0:
                if k - people[j] < 0:
                    break
                k -= people[j]
                j -= 1
                s -= 1
            # check if we can fit any remainig lighter people
            while s and i < N:
                if k - people[i] < 0:
                    break
                k -= people[i]
                i += 1
                s -= 1
            k = cap
            s = 2
            ans += 1
        
        return ans
            


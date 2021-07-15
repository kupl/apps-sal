class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        if n < 2: return 0
        
        ages.sort()
        
        mins = [0] * n
        pairs = [0] * n
        
        mins[0] = ages[0] / 2 + 7
        
        for i in range(1, n):
            mins[i] = (ages[i] - ages[i-1]) / 2 + mins[i-1]
            
            if ages[i-1] <= mins[i]:
                continue
            
            if mins[i] == mins[i-1]:
                pairs[i] = pairs[i-1] + 2
                continue

            j = i - 1
            while j >= 0 and ages[j] > mins[i]:
                pairs[i] += 1
                if ages[j] == ages[i]: pairs[i] += 1
                j-=1

        return sum(pairs)

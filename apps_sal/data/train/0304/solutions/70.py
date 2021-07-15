'''
PASS
[1, 2, 32, 32, 40, 41, 50]
[1, 2, 50]
[1, 2, 40, 41, 50] 
[40, 41, 50]
[16,16]
[6, 6]
'''

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        '''
        Observation: ages might be long (20,000), but there are only 120
        possible values for ages.
        '''
        
        ageCounts = Counter(ages)
        numRequests = 0
        
        '''
        [8,85,24,85,69]
        '''
        
        for a in range(1, 121):                
            if ageCounts[a] > 0:
                exclLowerBound = 0.5*a + 7
                lowerBound = ceil(exclLowerBound)
            
                if lowerBound == exclLowerBound:
                    lowerBound += 1
                    
                for a2 in range(lowerBound, a):
                    # multiply by ageCounts[a], each instance will send FR
                    numRequests += ageCounts[a2]*ageCounts[a]
                    
                if lowerBound <= a: # 16, 16, 16
                    # each instance will send FR to all the others
                    numRequests += ageCounts[a]*(ageCounts[a] - 1)
            
        return numRequests


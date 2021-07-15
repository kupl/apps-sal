class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        '''
        Algorithm
        ---------
        We first count the frequency of the ages
        '''
        def friendRequests(age_a, age_b):
            if age_b <= (0.5 * age_a + 7) or age_b > age_a:
                return False
            return True
        age_groups = collections.Counter(ages)
        total_requests = 0
        
        for age_a, count_a in list(age_groups.items()):
            for age_b, count_b in list(age_groups.items()):
                if friendRequests(age_a,age_b):
                    total_requests += count_a * count_b
                    
                    # if both candidates are the same, we reduce total
                    # requests by one of their frequencies
                    if age_a == age_b:
                        total_requests -= count_a
        return total_requests
            


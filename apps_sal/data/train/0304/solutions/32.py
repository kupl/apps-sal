# id(index) -> age
# age1 <= 7 + 0.5 age2
# age1 > age2
#age1 > 100 and age b < 100
# no selfloop,
#A request does not mean B reqeust A

def count_smaller_than(ages, target): # 1,15,17
    left = 0 # 1
    right = len(ages) - 1 # 0
    
    # 1 5 6 11 all elements smaller than  target 7
    # 1  [5] [6  [11] L = 3 R= 3 --> L = 3 R = 2 L -1
    #           L = 4 R = 3
  # [5] [6] 11 12 0 -> 0 0 -> -1
    # 5 6 | [6] 6 7 
    while left <= right:
        mid = left+(right-left)//2 # 15 # 1
        if ages[mid] < target: # 15 < 15
            left = mid+1        
        # elif ages[mid] == target and ages[a_index] == ages[mid]:
        #     right = mid - 1
        else:# ages[mid] >= target:
            right = mid -1 # 0 
            
    return left # 0 - 1
            
    # edge case [16,16]
    
    

import math
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        #brute force
        #we loop on friends A
            # we loop again B
                # increment if a request B or B requests A
                
                # time o(n^2), space o(1)
                
        #A < B
        # --> check only once not twice because second one is always false
        #whenever B > 100 and A < 100 --> recursve
        # O(N^2)
        
        #A --> 10 ---> [maximum length we make friends of] --> we search for that in the array and then we return
        # nlogn --> sort
        # n * logn (Binary search) to get the count
        
        ages.sort() # sort in ascending order
        friend_requests = 0
        
        #[1,17,18]
        for i in range(len(ages)):
            age_a = ages[i]  # 16
            
            # max_age_b = max(age_a,) # age_a = 9 -> 4.5 + 7 -> 11.5
            # 0 
            
            # 0 1 2 3 
            # 1 * 0.5 + 7 -> 7
            smaller_than = count_smaller_than(ages, math.floor(0.5 * age_a) + 8) # these are the ones to exclude, if it's
            smaller_than_i = count_smaller_than(ages, age_a+1)
            
            a_requests = max(0, smaller_than_i - 1 - smaller_than)  #(itself)
            
            friend_requests += a_requests
            
        return friend_requests
            


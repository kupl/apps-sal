class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        #happy owner means happy customer as well 
        happy_owner_cust = 0 
        
        for pos in range(len(customers)):
            if grumpy[pos] == 0: #happy owner 
                happy_owner_cust += customers[pos]
                customers[pos] = 0 
        
        
        #then build upon using the grumpy owner power. 
        
        calming_owner_cust = 0 
        best_calmed_cust = 0 
        
        for end in range(len(customers)): 
            calming_owner_cust += customers[end]
  
            
            
            if end >= X: #subtract out the extra calming technique from the owner 
                calming_owner_cust -= customers[end - X]
                
            best_calmed_cust = max(best_calmed_cust, calming_owner_cust)
            
            
            
            
        return happy_owner_cust + best_calmed_cust
    
# #TRY 8/10/2020 
# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         #Input: Customers[i] how many customers enter for that exact minute 
            
#         #Constraint 
#         #owner -> opens store up to customers.len()
#         #Every minute there are customers entering the store. And all those customers leave after the end of the minute 
        
#         #If owner is grumpy on i-th minute grumpy[i] = 1 else grumpy[i] = 0. When the bookstore owner is angry 
#         #The customers of that minute aren't satisfied else if owner isn't grumpy then customers are happy. 
        
#        # Bookstore owner can be NOT angry for X minutes but can use it ONLY once. 
       
#         #WANT: max number of customers that are happy throughout the day. 
        
        
#         minutes_opened = len(customers) 
#         customer_happy_time = 0 
        
#         #Try to basically keep your grumpy minutes down based on the highest number of customers there are. 
        
#         start = 0 
#         end = 0 
#         rush_hour = collections.deque() #this is based on the most amount of customers. 
#         calm_owner = collections.deque()
#         #Our best number of customer being happy will be based on the largest amount of customers
#         #That's our best bet. 
#         while end < minutes_opened: 
#             if customers[end] == 0: #No Customers go in owner can be angry 
#                 end += 1 
#                 continue 
                
#             cur_happy_time += customers[end]
#             if grumpy[end] == 1: #owner angry = customer angry: Just try calming here then. 
                
                
                
#             rush_hour.append(end)

# class Solution():
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         m = s = tmp = 0
#         for i in range(len(customers)):
#             if not grumpy[i]: 
#                 s += customers[i]                # sum of satisfied customers
#                 customers[i] = 0 
#             else: tmp += customers[i]            # sum of grumpy customers 
#             if i>=X: tmp -= customers[i-X]       # remove the leftmost element to keep the sliding window with # of X
#             m = max(m, tmp)                      # max # of satisfied grumpy customers with a secret technique
#         return s+m
    
    
# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         # Part 1 requires counting how many customers
#         # are already satisfied, and removing them
#         # from the customer list.
#         #These customers are those who didn't have to fight with the owner to be happy.
#         already_satisfied = 0
#         for i in range(len(grumpy)):
#             if grumpy[i] == 0: #He's happy so add the customer. 
#                 already_satisfied += customers[i]
#                 customers[i] = 0 #set you back to zero to not visit you. When doing the offset for the window 
        
#         # Part 2 requires finding the optimal number
#         # of unhappy customers we can make happy.
#         best_we_can_make_satisfied = 0
#         current_satisfied = 0
#         for i, customers_at_time in enumerate(customers):
#             # if customers[i] == 0: CAN'T DO THIS CUZ WE'RE NOT UPDATING THE WINDOW THEN AT THIS POINT (I.E THE START WINDOW)
#             #     continue
#             #Add the customer so far
#             current_satisfied += customers_at_time # Add current to rolling total
#             if i >= X: # We need to remove some from the rolling total #We need to update and try the grumpy intervals to block out owner from 
#                 #Being grumpy so we can add these happy customers but at this point
#                 #There's too much calming power used by owner so we need to remove the beginning window of the current_satisifed. 
#                 current_satisfied -= customers[i - X]
#             best_we_can_make_satisfied = max(best_we_can_make_satisfied, current_satisfied)
        
#         # The answer is the sum of the solutions for the 2 parts.
#         return already_satisfied + best_we_can_make_satisfied
    
    
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        always_happy = 0  
        for pos in range(len(customers)): 
            if grumpy[pos] == 0: 
                always_happy += customers[pos]
                customers[pos] = 0 
                
        happy_use = 0 
        cur_happy_customers = 0 
 
        for pos in range(len(customers)): 
            cur_happy_customers += customers[pos]
            
            if pos >= X: 
                cur_happy_customers -= customers[pos - X]
                
            
            happy_use = max(happy_use, cur_happy_customers)
            
        return always_happy + happy_use 

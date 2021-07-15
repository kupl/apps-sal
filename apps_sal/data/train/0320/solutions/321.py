class Solution:
    def minOperations(self, nums):
        add_operations = {}
        result = 0
        max_m = 0
        
        
        for i in nums:
            current = i
            if current in add_operations:
                result += add_operations[current]
            else:
                add_amount = 0
                multiplying_amount = 0
                
                while current:
                    if current % 2:
                        add_amount += 1
                        current -= 1
                    else:
                        multiplying_amount += 1
                        current = current / 2
                max_m = max(max_m, multiplying_amount)
                result += add_amount
                add_operations[i] = add_amount
        return result + max_m
                        


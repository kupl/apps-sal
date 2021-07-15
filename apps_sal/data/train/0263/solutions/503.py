class Solution:
    def knightDialer(self, n: int) -> int:
        valid_positions = {
            (0, 0): 1,
            (1, 0): 2,
            (2, 0): 3,
            (0, 1): 4,
            (1, 1): 5,
            (2, 1): 6,
            (0, 2): 7,
            (1, 2): 8,
            (2, 2): 9,
            (1, 3): 0
        }
        
        mod_val = 10**9 + 7
        
        cache = {}
        def find_numbers(start, length):
            if start not in valid_positions:
                return 0
            x,y = start
            
            if (x,y,length) in cache:
                return cache[(x,y,length)]
                
            if length == n:
                return 1
            
            x,y = start
            nums_found = sum(
                        [find_numbers((x+1, y-2), length+1),
                        find_numbers((x+2, y-1), length+1),
                        find_numbers((x-1, y-2), length+1),
                        find_numbers((x-2, y-1), length+1),
                        find_numbers((x-2, y+1), length+1),
                        find_numbers((x-1, y+2), length+1),
                        find_numbers((x+2, y+1), length+1),
                        find_numbers((x+1, y+2), length+1)]
            ) % mod_val
            
            cache[(x,y,length)] = nums_found
            return nums_found
                
                
            
        numbers_found = 0
        for position in valid_positions:
            numbers_found += find_numbers(position, 1)
            numbers_found %= mod_val
            
        # print(sorted(nums))
        
        return numbers_found
            
        
        


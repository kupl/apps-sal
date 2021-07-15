class Solution:
    def __init__(self):
        self.total_min = 0
        self.change_map = {0:0}
        
    def changer(self, coins_obj, amount_obj):
        
        if amount_obj == 0:
            self.change_map[amount_obj] = 0
            return 0
        if min(coins_obj) > amount_obj:
            self.change_map[amount_obj] = -1
            return -1
            
        rev_coins_obj = list(reversed(coins_obj))
        for el in rev_coins_obj:
            if el <= amount_obj:
                if amount_obj-el in self.change_map.keys():
                    tmp = self.change_map[amount_obj-el]
                else:
                    tmp = Solution.changer(self,coins_obj,amount_obj-el)
                
                if tmp != -1:
                    key = tmp+1
                    if amount_obj not in self.change_map.keys():
                        self.change_map[amount_obj] = key
                    elif amount_obj in self.change_map.keys():
                        if key < self.change_map[amount_obj]:
                            self.change_map[amount_obj] = key
                
                

                
        if amount_obj not in self.change_map.keys():
            self.change_map[amount_obj] = -1
            return -1
        elif amount_obj in self.change_map.keys():
            return self.change_map[amount_obj]
                    
                        
    
    def coinChange(self, coins: List[int], amount: int) -> int:

            
        Solution.changer(self, coins, amount)
        # print(self.change_map,amount)

        return self.change_map[amount]

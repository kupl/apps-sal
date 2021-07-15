# BSF No.1
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         queue = [[0, 0]]
#         visited = {0}
#         step = 0
        
#         for node, step in queue:
#             for coin in coins:
#                 if node + coin in visited:
#                     continue
#                 if node + coin == amount:
#                     return step + 1
#                 if node + coin < amount:
#                     queue.append([node + coin, step + 1])
#                     visited.add(node + coin)
#         return -1
    
# BSF No.2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        level = seen = {0}
        number = 0
        while level:
            # print(level)
            if amount in seen:
                return number
            level = {pre_amount + coin for pre_amount in level for coin in coins if pre_amount + coin <= amount}
            seen.update(level)
            # print(seen)
            number += 1
        return -1
    # level = seen = {0}
    # number = 0
    # while level:
    #     if amount in level:
    #         return number
    #     level = {a+c for a in level for c in coins if a+c <= amount} - seen
    #     seen |= level
    #     number += 1
    # return -1 


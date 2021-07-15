class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        current_sums = {}
        current_sums[0] = 1
        new_sums = {}
        out = 0
        
        for die in range(1, d+1):
            for face in range(1, f+1):
                for summ in list(current_sums.keys()):
                    curr = summ+face
                    if curr == target and die == d:
                        out += current_sums[summ]
                    elif curr < target:
                        if curr in list(new_sums.keys()):
                            new_sums[curr] += current_sums[summ]
                        else:
                            new_sums[curr] = current_sums[summ] 
                    
            current_sums = new_sums
            # print(current_sums)
            new_sums = {}
        
        return out % (10**9 + 7)

        # need to go through from target backwards suubtracting face everytime and adding to possibilities
    
    
#         def helper(h, d, target):
#             # if target is too small or if it is out of range
#             if target <= 0 or target > (d * f):
#                 return 0
#             if d == 1:
#                 print(d,f,target)
#                 return 1        # no need to check if target is within reach; already done before
#             if (d, target) in h:
#                 return h[(d, target)]        # directly access from hash table
#             res = 0
#             for i in range(1, f + 1):
#                 res += helper(h, d - 1, target - i)       # check all possible combinations
#             h[(d, target)] = res
#             return h[(d, target)]
        
#         h = {}
#         return helper(h, d, target) % (10 ** 9 + 7)


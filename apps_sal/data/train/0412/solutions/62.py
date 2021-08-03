class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def count_for_roll(num_dice, curr_target):

            if num_dice == 0 and curr_target == 0:
                return 1

            if num_dice == 0 or curr_target == 0:
                return 0

            if (num_dice, curr_target) in memo:
                return memo[(num_dice, curr_target)]

            curr_count = 0

            for face in range(1, f + 1):

                new_target = curr_target - face

                if new_target < 0:
                    break

                curr_count += count_for_roll(num_dice - 1, new_target)

            memo[(num_dice, curr_target)] = curr_count
            return curr_count % mod

        memo = {}
        mod = 10**9 + 7

        return count_for_roll(d, target)


'''
d = 2, f = 6, t = 7

1
    1
    2
    3
    4
    5
    6 -> inc
    
2
    1
    2
    3
    4
    5 -> inc
    6 -> stop?
    
3 
    1
    2
    3
    4 -> inc
    5 -> stop
    
    

'''

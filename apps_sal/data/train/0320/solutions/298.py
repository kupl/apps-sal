class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # After having implemented minOperations_dumb_solution(), we realize that 
        # the number of op 1 we'll need to do is just the number of times we need
        # to divide the max even number we ever encounter to get it down to zero. 
        # Because, a division would reduce everyone by 2 and when the smaller even
        # numbers we see gets down to zero, it will no longer be affected. We only care
        # about dividing the biggest even number down to zero.
        cost = 0
        max_nb_op_1 = 0
        for i in range(len(nums)):
            nb_op_0 = nb_op_1 = 0
            x = nums[i]
            while x > 0:
                if x % 2 != 0:
                    nb_op_0 += x % 2
                    x -= x % 2
                if x > 0:
                    nb_op_1 += 1
                    x = x // 2
            cost += nb_op_0
            max_nb_op_1 = max(max_nb_op_1, nb_op_1)
        cost += max_nb_op_1
        return cost
    
    def minOperations_dumb_solution(self, nums: List[int]) -> int:
        # Key insight is if nums[i] is odd, there's no way we could have arrived at nums[i]
        # via op 1, i.e. by multiplying by 2 some previous value. So the only way we could
        # have gotten here is by using op 0, nums[i] % 2 times. That is we need to skim off
        # the remainder part that makes it non-even before we can consider using op 1.
        cost = 0
        while True:
            all_zeros = True
            all_evens = True
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                
                all_zeros = False
                if nums[i] % 2 != 0:
                    cost += nums[i] % 2
                    nums[i] = nums[i] - (nums[i] % 2)
                    all_evens = False
            
            if all_zeros:
                break
            while all_evens:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                    if nums[i] % 2 != 0:
                        all_evens = False
                cost += 1
                
        return cost
                    


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
        Find subarray[i:j] where i < j such that 
        (sum(arr) - sum(arr[i:j])) % p == 0

        This can be rewritten with c where c[i] is cumulative sum up to index i

        Note c[-1] refers to c[len(c)] in Python

        (c[-1] - (c[j] - c[i])) % p == 0 

        From Question: Subarray Sums Divisible by K
        this is the same as:

        (c[j] - c[i]) % p == c[-1] % p

        (c[j] - c[i]) % p == target

        c[j] - c[i] = p*n + target         where n is some number

        c[j] - p*n - target == c[i]

        (c[j] % p - p*n % p - target % p) % p == c[i] % p  

         mod both sides, (a + b) % n == (a % n + b % n) % n, thats why extra % p on LHS

        (c[j] % p - target % p) % p == c[i] % p

        (c[j] % p - (c[-1] % p) % p) % p == c[i] % p      expand out target

        (c[j] % p - (c[-1] % p)) % p == c[i] % p      mod rule: (a % b) % b = a % b

        (c[j] % p - target) % p == c[i] % p

        c[i] % p will be stored in the hashmap along with the index
        Which is why we query the LHS, for it

        '''
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        target = nums[-1] % p
        if target == 0:
            return 0

        ans = len(nums)
        remainders = {0: -1}

        for j in range(len(nums)):
            complement = (nums[j] % p - target) % p

            if complement in remainders:
                ans = min(ans, j - remainders[complement])

            remainders[nums[j] % p] = j

        return ans if ans < len(nums) else -1

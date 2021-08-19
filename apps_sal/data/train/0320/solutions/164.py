class Solution:

    def minOperations(self, nums: List[int]) -> int:
        add_count = 0
        mut_count = 0

        def get_add_mut_count(n):
            add = mut = 0
            while n:
                if n % 2:
                    n -= 1
                    add += 1
                else:
                    n /= 2
                    mut += 1
            return (add, mut)
        for n in nums:
            (a, m) = get_add_mut_count(n)
            add_count += a
            mut_count = max(mut_count, m)
        return add_count + mut_count

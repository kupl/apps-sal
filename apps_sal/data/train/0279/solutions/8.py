class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ""
        nums = list(range(1, n + 1))
        m = self.factorial(n - 1)

        while len(nums) > 1:
            print("n=", n, ", k=", k, " m=", m)
            remainer = k % m
            if remainer == 0:
                remainer = m
            index = (k - remainer) // m
            print(index)
            ans += str(nums[index])
            nums.remove(nums[index])
            k = remainer
            n -= 1
            m = m // n

        ans += str(nums[0])
        return ans

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

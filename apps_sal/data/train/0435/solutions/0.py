# Calculate the prefix sum and count it.
# In c++ and java, a % K + K takes care of the cases where a < 0.
# Python

class Solution: 
    def subarraysDivByK(self, A, K):
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
    
# If a subarray is divisible by K, it has to be a multiple of K

# a-b=n*k, a = running total, b = any previous subarray sum, same as original prefix sum problems.

# We want to solve for b, so using basic algebra, b=a-n*k

# We don't know what n is, so we can get rid of n by modding every element by k
# (b%k) = (a%k) - (n*k)%k

# since n*k is a multiple of k and k goes into it evenly, the result of the (n *k)%k will be 0

# therefore
# b%k = a%k

# is the same as the formula we defined earlier, a-b=n*k

# where b = running total, a = any previous subarray sum

# So we just have to see if running total mod k is equal to any previous running total mod k


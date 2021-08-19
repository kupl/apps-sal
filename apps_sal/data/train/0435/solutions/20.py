class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        Algorithm
        ---------
        We will keep track of the running sum s. We then take the
        modulo of the sum and record its frequency in a hash table.

        After the first pass the number of subarrays divisible by K
        is the sum of the frequencies of the remainders choose 2 -> c *(c - 1)//2
        '''

        # Hash table to store modulo
        ht = [0] * K

        sum = 0
        for num in A:
            sum += num
            ht[sum % K] += 1

        # handle the case of 0 remainder -> n * (n - 1) // 2 + n
        results = ht[0]

        for c in ht:
            results += (c * (c - 1)) // 2
        return results

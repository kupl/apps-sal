class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        primes = []
        available = [True for _ in range(100000)]
        available[0] = False
        available[1] = False
        k = 0

        while True:
            while k < len(available) and available[k] == False:
                k += 1
            if k == len(available):
                break
            primes.append(k)
            n = 1
            while n * k < len(available):
                available[n * k] = 0
                n += 1

        def factorize(x):
            result = collections.Counter()
            if x == 1:
                return result
            for p in primes:
                if x % p == 0:
                    result[p] += 1
                    return result + factorize(x // p)

        print(factorize(7 * 13 * 5))

        fac1 = [factorize(n) for n in nums1]
        fac2 = [factorize(n) for n in nums2]
        '''

        prod1 = collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                prod1[nums1[i] * nums1[j]] += 1

        prod2 = collections.defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                prod2[nums2[i] * nums2[j]] += 1

        count = 0
        for n in nums1:
            count += prod2[n * n]

        for n in nums2:
            count += prod1[n * n]

        return count

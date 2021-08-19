class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        A = collections.defaultdict(int)
        B = collections.defaultdict(int)
        ans = 0
        for i in nums1:
            a = i * i
            B.clear()
            for j in nums2:
                b = j * j
                x = a / j
                if x in B:
                    ans += B[x]
                y = b / i
                if y in A:
                    ans += A[y]
                B[j] += 1
            A[i] += 1
        return ans

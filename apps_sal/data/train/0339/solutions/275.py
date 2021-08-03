class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ret1 = self.check(nums1, nums2)
        ret2 = self.check(nums2, nums1)

        return (ret1 + ret2)

    def check(self, n1: List[int], n2: List[int]):
        count_n2_org = Counter(n2)
        cnt = 0

        for i in range(len(n1)):
            square = n1[i]**2
            count_n2 = count_n2_org.copy()

            for j in range(len(n2)):
                if (square % n2[j] == 0):
                    target = square // n2[j]

                    if (count_n2[target] > 0):
                        count_n2[n2[j]] -= 1
                        cnt += count_n2[target]

        return cnt

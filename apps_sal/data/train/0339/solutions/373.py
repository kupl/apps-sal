from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        nums1.sort()
        nums2.sort()

        def search(array1, array2):
            result = 0
            hashtable = defaultdict(int)

            for i in array2:
                hashtable[i] += 1

            for a in array1:
                squared = a ** 2

                met = []
                for i in list(hashtable.keys()):
                    if i not in met:
                        if squared % i == 0:
                            complement = squared // i
                            if complement != i:
                                result += hashtable[i] * hashtable[complement]
                                met.append(complement)
                            else:
                                met.append(i)
                                result += sum([j for j in range(hashtable[i])])

            return result

        count += search(nums1, nums2)
        count += search(nums2, nums1)

        return count

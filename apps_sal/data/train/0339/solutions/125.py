class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(arr, match):
            n = len(arr)
            cnt = 0
            for i in range(n):
                for j in range(i + 1, n):
                    val = math.sqrt(arr[i] * arr[j])
                    if match.get(val):
                        cnt += match[val]
            return cnt
        (freq1, freq2) = (collections.Counter(nums1), collections.Counter(nums2))
        return count(nums1, freq2) + count(nums2, freq1)

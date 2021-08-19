class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(arr, match):
            n = len(arr)
            cnt = 0
            for i in range(n):
                for j in range(i + 1, n):
                    val = math.sqrt(arr[i] * arr[j])
                   # print(val)
                    if match.get(val):
                        cnt += match[val]
            return cnt

        # square1,square2=collections.defaultdict(int),collections.defaultdict(int)
        # duplet1,duplet2=collections.defaultdict(int),collections.defaultdict(int)

        freq1, freq2 = collections.Counter(nums1), collections.Counter(nums2)
        # Num1,Num2=list(freq1.keys()),list(freq2.keys())
       # return 1
        return count(nums1, freq2) + count(nums2, freq1)

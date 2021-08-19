class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for n1 in nums1:
            n1 = n1 ** 2
            visited = collections.defaultdict(int)
            for n2 in nums2:
                if n1 % n2 == 0 and visited[n1 // n2] > 0:
                    res += visited[n1 // n2]
                visited[n2] += 1
        for n2 in nums2:
            n2 = n2 ** 2
            visited = collections.defaultdict(int)
            for n1 in nums1:
                if n2 % n1 == 0 and visited[n2 // n1] > 0:
                    res += visited[n2 // n1]
                visited[n1] += 1
        return res

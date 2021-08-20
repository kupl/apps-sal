class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.helper(nums1, nums2) + self.helper(nums2, nums1)

    def helper(self, arr1, arr2):
        res = 0
        for num in arr1:
            res += self.twoProduct(num * num, arr2)
        return res

    def twoProduct(self, target, arr):
        visited = {}
        res = 0
        for num in arr:
            if not num:
                continue
            if target % num == 0 and target // num in visited:
                res += visited[target // num]
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1
        return res

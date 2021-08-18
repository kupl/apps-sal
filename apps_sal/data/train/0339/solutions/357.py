class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def f(u, v):
            v = Counter(float(i) for i in v)
            for x in u:
                w = x * x

                for y in v:
                    if y == x:
                        n = v[y]
                        yield n * (n - 1)
                        continue
                    z = w / y
                    if z in v:
                        yield v[y] * v[z]

        a = sum(f(nums1, nums2)) + sum(f(nums2, nums1))
        return a // 2

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def f(u, v):
            v = Counter(float(i) for i in v)
            # print(f'u {u} v {v}')
            for x in u:
                w = x * x
                
                for y in v:
                    if y == x:
                        n = v[y]
                        # print(f'!! x {x} y {y} n {n}')
                        yield n * (n-1)
                        continue
                    z = w / y
                    if z in v:
                        # print(f'!! x {x} y {y} z{z} v[y] * v[z] {v[y] * v[z]}')
                        yield v[y] * v[z]
        
        # a = f(nums1, nums2)
        # b = f(nums2, nums1)
        # print(sum(a), sum(b))
        a = sum(f(nums1, nums2)) + sum(f(nums2, nums1))
        return a // 2

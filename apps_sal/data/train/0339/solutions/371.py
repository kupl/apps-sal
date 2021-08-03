class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find(target, arr):
            seen = Counter()
            count = 0
            for a in arr:
                if target % a == 0:
                    count += seen[target // a]
                seen[a] += 1
            return count

        @lru_cache(None)
        def twoProduct1(target):
            return find(target, nums1)

        @lru_cache(None)
        def twoProduct2(target):
            return find(target, nums2)

        return sum(twoProduct2(a * a) for a in nums1) + sum(twoProduct1(a * a) for a in nums2)

    def numTriplets2(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1
        res = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]
                if p in d2:
                    res += d2[p]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                p = nums2[i] * nums2[j]
                if p in d1:
                    res += d1[p]
        return res

    def numTriplets3(self, A1: List[int], A2: List[int]) -> int:
        A1.sort()
        A2.sort()
        C1, C2 = collections.Counter(A1), collections.Counter(A2)
        # print(A1,A2,C1,C2)
        res = 0
        N1, N2 = len(A1), len(A2)
        seen = set()
        for i, x in enumerate(A1):
            for j, y1 in enumerate(A2):
                if x * x < y1:
                    break
                # if y1 in seen:continue
                y2 = x * x // y1
                if x * x % y1 == 0 and y2 in C2:
                    c = C2[y2]
                    # print(x,y1,c)
                    if x == y1:
                        res += comb(c, 2)  # if c>1 else 0
                    else:
                        res += c * C2[y1]
                    seen |= {y1, y2}
                    break
        # print(res)
        seen = set()
        for x in A2:
            for y1 in A1:
                if x * x < y1:
                    break
                # if y1 in seen:continue
                y2 = x * x // y1
                if x * x % y1 == 0 and y2 in C1:
                    c = C1[y2]
                    # print('-',x,y1,c)
                    if x == y1:
                        res += comb(c, 2)  # if c>1 else 0
                    else:
                        res += c * C1[y1]
                    seen |= {y1, y2}
                    break
        return res

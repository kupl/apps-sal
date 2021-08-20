import heapq


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = [0] + nums[:]
        for i in range(1, len(s)):
            s[i] += s[i - 1]
        ss = [0] + s[:]
        for i in range(1, len(ss)):
            ss[i] += ss[i - 1]

        def findKthSum(k):
            (l, r) = (0, s[-1])
            while l < r:
                mid = (l + r) // 2
                if countSumsLeq(mid) < k:
                    l = mid + 1
                else:
                    r = mid
            return l

        def countSumsLeq(sv):
            c = 0
            l = 0
            for r in range(len(s)):
                while s[r] - s[l] > sv:
                    l += 1
                c += r - l
            return c

        def getSumsUpToKth(k):
            sv = findKthSum(k)
            rv = 0
            l = 0
            for r in range(len(s)):
                while s[r] - s[l] > sv:
                    l += 1
                rv += sum([s[r] - s[ll] for ll in range(l, r)])
            return rv - (countSumsLeq(sv) - k) * sv
        return (getSumsUpToKth(right) - getSumsUpToKth(left - 1)) % (10 ** 9 + 7)

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # stack + binary search
        descends = [(A[0], 0)]

        def bs(t):
            lo, hi = 0, len(descends) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if descends[mid] > t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        rint = 0
        for i in range(1, len(A)):
            if A[i] < descends[-1][0]:
                descends.append((A[i], i))
            else:
                left = bs((A[i], i))
                # print(i, left, descends[left][1], descends)
                rint = max(rint, i - descends[left][1])
        return rint

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        size = len(A)
        l, r, total, cnt = [0] * 4
        if S == 0:
            l = 1
            for x in A:
                if x == 0:
                    cnt += l
                    l += 1
                else:
                    l = 1
            return cnt
        while r < size and total < S:
            total += A[r]
            r += 1
        if r == size and total < S:
            return 0
        while r < size:
            cnt1, cnt2 = 1, 1
            while l < r and A[l] == 0:
                l += 1
                cnt1 += 1
            while r < size and A[r] == 0:
                r += 1
                cnt2 += 1
            cnt += cnt1 * cnt2
            l += 1
            r += 1
        if A[-1] == 1:
            cnt += 1
            while l < size and A[l] == 0:
                cnt += 1
                l += 1
        return cnt

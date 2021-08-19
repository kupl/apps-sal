class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < 1:
            return 0

        result = 0
        fc = Counter()
        c = Counter()
        l = 0
        fr = 0
        r = 0
        while l < n:
            while fr < n and len(fc) < K:
                fc[A[fr]] += 1
                fr += 1
            while r < n:
                if A[r] not in c and len(c) >= K:
                    break
                c[A[r]] += 1
                r += 1
            #print(c, l, fr, r)
            if len(c) == K:
                result += r - fr + 1
            fc[A[l]] -= 1
            if fc[A[l]] == 0:
                del fc[A[l]]
            c[A[l]] -= 1
            if c[A[l]] == 0:
                del c[A[l]]
            l += 1
            print('c', l, r)

        return result

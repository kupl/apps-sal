class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def sop(A, H, K):
            if (K == 0):
                return False
            count = 0
            for i in A:
                if (i % K == 0):
                    count += i // K
                else:
                    count += i // K + 1

            if count <= H:
                return True

            return False

        l = sum(piles) // H
        r = max(piles)
        print((l, r))

        print((sop(piles, H, l)))

        if len(piles) == 1:
            return l + 1

        m = (l + r) // 2
        while (l <= r):
            if (sop(piles, H, l) == False) and (sop(piles, H, l + 1) == True):
                return l + 1

            if (sop(piles, H, r - 1) == False) and (sop(piles, H, r) == True):
                return r

            if sop(piles, H, m) == False:
                l = m
                m = (l + r) // 2
            else:
                r = m
                m = (l + r) // 2

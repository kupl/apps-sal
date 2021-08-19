class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # piles = [30,11,23,4,20]
        # H = 6

        #         piles =[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]

        #         H = 823855818

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
            # print(m)
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

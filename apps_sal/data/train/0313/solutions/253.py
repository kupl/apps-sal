class Solution:
    def make_bouquets(self, A, day, k):
        cnt, consec = 0, 0
        for i in A:
            if day >= i:
                consec += 1
            else:
                consec = 0
            if consec == k:
                cnt += 1
                consec = 0
        return cnt

    def minDays(self, A, m, k):
        l, r = min(A), max(A)
        print(f'{l=} | {r=}')
        while r > l:
            mid = (l + r) // 2
            if self.make_bouquets(A, mid, k) >= m:
                r = mid
            else:
                l = mid + 1
        print(f'{l=} | {r=}')
        if self.make_bouquets(A, l, k) >= m:
            return l
        else:
            return -1

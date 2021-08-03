class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay or m * k > len(bloomDay):
            return -1
        mx = max(bloomDay)
        mn = min(bloomDay)
        l = mn
        r = mx
        not_possible = False
        while l < r:
            day = (l + r) // 2
            p = self.works(day, bloomDay, m, k)
            if p:
                r = day
            else:
                l = day + 1
            # if l >= r and not p:
            #    not_possible = True

        return l if not not_possible else -1

    def works(self, day, arr, m, k):
        ktmp = k
        for i in range(len(arr)):
            n = arr[i]
            if n <= day:
                ktmp -= 1
                if ktmp == 0:
                    ktmp = k
                    m -= 1
                if m == 0:
                    return True
            else:
                ktmp = k
        return False

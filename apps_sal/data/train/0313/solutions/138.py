class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def count(l, i):
            c, count = 0, 0
            for j in l:
                if(j <= i):
                    c += 1
                elif(j > i):
                    count += c // k
                    c = 0
            return count + c // k
        l = bloomDay[:]
        if((len(l) // k) < m):
            return -1
        l1 = min(l)
        r = max(l)
        while(l1 < r):
            mid = l1 + (r - l1) // 2
            if(count(l, mid) >= m):
                r = mid
            else:
                l1 = mid + 1
        return l1

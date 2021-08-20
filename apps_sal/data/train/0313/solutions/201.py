class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def canMake(bloomDay, m, k, day):
            bloom = []
            for bday in bloomDay:
                if bday <= day:
                    bloom.append(1)
                else:
                    bloom.append(-1)
            (r, cur, cnt) = (0, 0, 0)
            while r < len(bloomDay):
                if bloom[r] == 1:
                    cur += 1
                    if cur == k:
                        cnt += 1
                        cur = 0
                        if cnt == m:
                            return True
                else:
                    cur = 0
                r += 1
            return False
        if m * k > len(bloomDay):
            return -1
        (left, right) = (min(bloomDay), max(bloomDay))
        while left < right:
            mid = (left + right) // 2
            if not canMake(bloomDay, m, k, mid):
                left = mid + 1
            else:
                right = mid
        return left

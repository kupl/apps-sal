class Solution:
    def minDays(self, n: int) -> int:
        last = {n}
        cnt = 0
        while 1:
            neo = set()
            for i in last:
                if i == 0:
                    return cnt
                neo.add(i - 1)
                if i % 2 == 0:
                    neo.add(i//2)
                if i % 3 == 0:
                    neo.add(i // 3)
            cnt += 1
            last = neo


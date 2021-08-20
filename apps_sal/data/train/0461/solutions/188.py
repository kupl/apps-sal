class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 0:
            return 0
        maxx = 0
        cache = {}
        for i in range(n):
            curr = i
            count = 0
            while curr != headID:
                curr = manager[curr]
                count += informTime[curr]
                if curr in cache:
                    count += cache[curr]
                    break
            cache[i] = count
            maxx = max(maxx, count)
        return maxx

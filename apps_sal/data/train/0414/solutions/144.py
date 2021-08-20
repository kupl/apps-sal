class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        c = 0
        m = arr[0]
        for x in arr:
            if x == m:
                pass
            elif x > m:
                m = x
                c = 1
            else:
                c += 1
            if c == k:
                return m
        return m

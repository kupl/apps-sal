class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt = 0
        a = arr
        i = 0
        n = len(a)
        for j in range(1, n):
            if a[i] > a[j]:
                cnt += 1
            else:
                i = j
                cnt = 1
            if cnt >= k:
                return a[i]
        return a[i]

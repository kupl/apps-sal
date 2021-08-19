class Solution:
    """
     [10,10,10,10,10,100], 
     m = 3, k = 2


    """

    def checkBl(self, arr, day, m, k):
        cnt = 0
        i = 0
        start = 0
        N = len(arr)
        while i < N:
            if arr[i] <= day:
                if start == k - 1:
                    start = 0
                    cnt += 1
                else:
                    start += 1
            else:
                start = 0
            if cnt == m:
                return True
            i += 1
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m == 0:
            return 0
        if m * k > len(bloomDay):
            return -1
        max_bd = float('-inf')
        min_bd = float('inf')
        for i in bloomDay:
            max_bd = max(max_bd, i)
            min_bd = min(min_bd, i)
        l = min_bd
        r = max_bd
        while l < r:
            mid = (l + r) // 2
            if self.checkBl(bloomDay, mid, m, k):
                r = mid
            else:
                l = mid + 1
        return l

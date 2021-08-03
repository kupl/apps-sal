class Solution:
    def getWinner(self, a: List[int], target: int) -> int:
        count_prev = 0
        count_after = 0
        n = len(a)
        i = 0
        j = 1
        while i < n - 1:
            while(a[i] > a[j] and j < (n - 1) and count_prev < target):
                count_prev += 1
                j += 1
            if(count_prev == target):
                return a[i]
            else:
                i = j
                j = j + 1
                count_prev = 1
        return max(a)

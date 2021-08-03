class Solution:
    def isSafe(self, lst, m, key):
        n = len(lst)
        pre = lst[0]
        index = 1
        while(index < n):
            while(index < n and lst[index] - pre < key):
                index += 1

            m -= 1
            if(m == 0):
                return True
            if(index == n):
                return False
            pre = lst[index]

        return False

    def maxDistance(self, lst: List[int], m: int) -> int:
        lst.sort()
        n = len(lst)
        low = 0
        high = lst[-1] - lst[0]
        ans = 0

        while(low <= high):
            mid = (low + high) // 2
            if(self.isSafe(lst, m, mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

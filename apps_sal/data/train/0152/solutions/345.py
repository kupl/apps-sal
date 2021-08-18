class Solution:
    def fun(self, arr, dist):
        pos = arr[0]
        cows = 1
        for i in range(1, len(arr)):
            e = arr[i]
            if e - pos >= dist:
                pos = e
                cows += 1
            if cows == self.m:
                return True
        return False

    def bs(self, arr):
        lef = 0
        rit = arr[-1]
        while lef < rit:
            mid = (lef + rit) // 2
            me = self.fun(arr, mid)
            nex = self.fun(arr, mid + 1)
            if me and not nex:
                return mid
            elif me and nex:
                lef = mid + 1
            else:
                rit = mid - 1
        return lef

    def maxDistance(self, position: List[int], m: int) -> int:
        self.m = m
        position.sort()
        return self.bs(position)

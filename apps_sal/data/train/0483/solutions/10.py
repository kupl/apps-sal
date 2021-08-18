class Solution:
    def get_ans(self, l, r):
        return (r - l) * min(self.__height[l], self.__height[r])

    def rmove(self, l):
        for i in range(l + 1, len(self.__height)):
            if self.__height[i] > self.__height[l]:
                return i
        return 10000000

    def lmove(self, r):
        for i in range(r - 1, -1, -1):
            if self.__height[i] > self.__height[r]:
                return i
        return -1

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.__height = height
        ans = 0
        L = 0
        R = len(height) - 1
        while L < R:
            ans = max(ans, self.get_ans(L, R))
            if height[L] <= height[R]:
                L = self.rmove(L)
            else:
                R = self.lmove(R)
        return ans

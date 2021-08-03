class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        def helper(ll, num):
            '''
            ll is a sorted list
            num is either h or w
            '''
            ll.append(num)
            ans = ll[0]
            for i in range(1, len(ll)):
                if ll[i] - ll[i - 1] > ans:
                    ans = ll[i] - ll[i - 1]
            return ans

        return int((helper(horizontalCuts, h) * helper(verticalCuts, w)) % (1e9 + 7))

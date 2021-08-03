class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        c = 0
        ans = 0
        for i in range(len(seats)):
            if seats[i]:
                if ans == 0 and c > 0 and c == i:
                    ans = c
                elif (c + 1) // 2 > ans:
                    ans = (c + 1) // 2
                c = 0
            else:
                c += 1
        ans = max(c, ans)
        return ans

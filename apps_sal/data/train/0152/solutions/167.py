class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def place(d):
            print(d)
            ans = 1
            pos = position[0] + d
            j = 1

            while pos <= position[-1]:
                while j < len(position) and position[j] < pos:
                    j += 1
                if j == len(position):
                    break
                ans += 1
                pos = position[j] + d
                j += 1

            print('ans')
            print(ans)
            return ans

        l = 0
        r = position[-1] - position[0]

        while l <= r:
            mid = (l + r) // 2
            if place(mid) >= m:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1

class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(position, mid):
            i = position[0]
            count = 0
            for j in position:
                if j - i >= mid:
                    count += 1
                    i = j
            return count + 1
        l = 0
        position.sort()
        r = position[-1]
        while r > l + 1:
            mid = math.ceil((l + r) / 2)
            print(mid)
            k = check(position, mid)
            if k < m:
                r = mid
            else:
                l = mid
        return l

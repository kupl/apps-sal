class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def check(dist: int) -> bool:

            curr = position[0]
            count = 1

            for i in range(len(position)):

                if (abs(position[i] - curr) >= dist):

                    curr = position[i]
                    count += 1

                    if (count >= m):
                        return True

                if(i == (len(position) - 1)):

                    if (count >= m):
                        return True
                    else:
                        return False

        lo = 1
        hi = (max(position) - min(position))

        while (lo < hi):

            mid = lo + ((hi - lo + 1) // 2)

            if(check(mid)):

                lo = mid

            else:
                hi = mid - 1

        return (lo)

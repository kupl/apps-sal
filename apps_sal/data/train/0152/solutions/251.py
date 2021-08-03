class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def feasible(d, position):
            # print(\"Check d: \", d)
            balls = [position[0]]
            placed = 1
            i = 1
            while i <= len(position) - 1:
                if position[i] - balls[-1] >= d:
                    balls.append(position[i])
                    # print(balls)
                    placed += 1
                    if placed == m:
                        return True
                i += 1
            return False

        position.sort()

        left, right = 1, max(position)

        while left < right:
            mid = right - (right - left) // 2
            if feasible(mid, position):
                left = mid
            else:
                right = mid - 1
        return left

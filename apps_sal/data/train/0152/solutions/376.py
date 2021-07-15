class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        r = 1 + position[-1] - position[0]
        while l + 1 < r:
            med = (l + r) // 2
            cnt = 0
            pre = position[0] - 2*med
            for x in position:
                if x - pre >= med:
                    pre = x
                    cnt += 1
            if cnt >= m: l = med
            else: r = med
        return l

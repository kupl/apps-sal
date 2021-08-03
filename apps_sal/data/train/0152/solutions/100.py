class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        delta = []
        for i in range(len(position) - 1):
            delta.append(position[i + 1] - position[i])

        lo = min(delta)
        hi = sum(delta)
        m -= 1

        def isPossible(minForce):
            total = 0
            count = 0
            for d in delta:
                total += d
                if total >= minForce:
                    count += 1
                    total = 0
                    if count == m:
                        return True
            return False

        while lo <= hi:
            mid = (lo + hi) // 2
            if isPossible(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo - 1

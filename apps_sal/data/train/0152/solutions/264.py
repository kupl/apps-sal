class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def feasible(min_req_dist, b):
            i = 0
            prev_pos = None
            while i < len(position) and b > 0:
                if prev_pos == None or position[i] - prev_pos >= min_req_dist:
                    b -= 1
                    prev_pos = position[i]
                i += 1
            return b == 0

        # This is a fantastic example of establishing a monotonic predicate and
        # squeeze from the right side of the search space (instead of the usual left-side)
        position.sort()
        low = 1
        high = position[-1]
        while low < high:
            # Since we constantly trying to see if we could find a feasible solution that's
            # greater than the current one, we want to always make progress by advancing
            # mid to the right. (low + high) // 2 + 1 guarantees this, even when we have
            # just two elements. mid will be pointing at high. Otherwise we'd get an infinite
            # loop with (low + high) // 2
            mid = (low + high) // 2 + 1
            if feasible(mid, m):
                low = mid
            else:
                high = mid - 1
        return low

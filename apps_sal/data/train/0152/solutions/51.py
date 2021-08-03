class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def ifvalid(diff, num_division):
            selected = 0
            cur = position[0]
            for i, f in enumerate(position):
                if selected >= num_division:
                    return True
                if (f - cur) >= diff:
                    selected += 1
                    cur = position[i]
                else:
                    if i == len(position) - 1:
                        return False
            return selected >= num_division

        def search(l, r):
            while l < r:
                mid = l + (r - l) // 2
                if not ifvalid(mid, m - 1):
                    r = mid
                else:
                    l = mid + 1
            return l - 1

        max_diff = (position[-1] - position[0]) // (m - 1) + 1
        return search(1, max_diff + 1)

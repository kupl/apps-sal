class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def helper(d):
            cnt = 1
            cur = position[0]
            for i in range(1, len(position)):
                if cur + d <= position[i]:
                    cur = position[i]
                    cnt += 1
            return cnt

        l, r = 0, position[-1] - position[0]
        res = -float('inf')
        while l <= r:
            # print(l, r)
            # if l == r and helper(l) == m:
            #     return l
            mid = (l + r) >> 1
            if helper(mid) == m:
                res = max(mid, res)
                l = mid + 1
            elif helper(mid) > m:
                # res = max(mid, res)
                l = mid + 1
            else:
                r = mid - 1
        return max(res, l - 1)

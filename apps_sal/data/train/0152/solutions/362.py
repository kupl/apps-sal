class Solution:
    import bisect

    def maxDistance(self, position: List[int], m: int) -> int:
        l, r = 1, max(position) - min(position)
        if m == 2:
            return r
        position = sorted(position)

        def fea(D):
            s = min(position)
            need = 1
            last = 1
            while(True):
                for i in range(last, len(position)):
                    if position[i] >= s + D:
                        need += 1
                        s = position[i]
                        last = i
                        break
                if last == len(position) - 1 or position[-1] < s + D:
                    break
            return need

        print((fea(2)))
        while(l < r):
            mid = l + (r - l) // 2
            if fea(mid) < m:
                r = mid
            else:
                l = mid + 1

        return l - 1

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        lt = []
        for hour in hours:
            if hour > 8:
                lt.append(1)
            else:
                lt.append(-1)
        seen = {}
        s = 0
        mx = 0
        for idx, ele in enumerate(lt):
            s += ele
            print((s, idx, mx))
            if s > 0:
                mx = max(mx, (idx + 1))
            else:
                if (s - 1) in seen:
                    i = seen[s - 1]
                    mx = max(mx, idx - i)
            if (s) not in seen:
                seen[s] = idx
        return mx

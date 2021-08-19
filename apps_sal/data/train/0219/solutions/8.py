class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if i > 8 else -1 for i in hours]
        hsh = {}
        vals = [0 for i in hours]
        sm = 0
        for i in range(len(hours) - 1, -1, -1):
            sm += hours[i]
            if sm > 0:
                vals[i] = max(vals[i], len(hours) - i)
            hours[i] = sm
            smo = hours[i] - 1
            if smo in hsh:
                v = hsh[smo]
                vals[i] = max(vals[i], v - i + vals[v])
            if hours[i] not in hsh:
                hsh[hours[i]] = i
        return max(vals)

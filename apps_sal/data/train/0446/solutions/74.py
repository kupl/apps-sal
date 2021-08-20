class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = {}
        for a in arr:
            if not a in m:
                m[a] = 1
            else:
                m[a] += 1
        m = dict(sorted(m.items(), key=lambda x: x[1]))
        count = 0
        for (key, value) in m.items():
            if value <= k:
                m[key] = 0
                k -= value
                count += 1
            else:
                break
        return len(m) - count

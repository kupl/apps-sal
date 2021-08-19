class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mapp = {}
        for item in arr:
            if item in list(mapp.keys()):
                mapp[item] += 1
            else:
                mapp[item] = 1
        sort_mapp = {c: v for (c, v) in sorted(list(mapp.items()), key=lambda x: x[1])}
        for (c, v) in list(sort_mapp.items()):
            if v - k > 0:
                sort_mapp[c] -= k
                break
            else:
                k = (v - k) * -1
                sort_mapp[c] = 0
                if k <= 0:
                    break
        count = 0
        for (c, v) in list(sort_mapp.items()):
            if v > 0:
                count += 1
        return count

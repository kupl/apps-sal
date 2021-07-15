class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        starts, ends = {}, {}
        res = None
        contributors = set()
        for i, pos in enumerate(arr):
            if pos-1 not in ends:
                l = pos
            else:
                l = ends[pos-1]
                del ends[pos-1]
                if l in contributors:
                    contributors.remove(l)
            if pos+1 not in starts:
                r = pos
            else:
                r = starts[pos+1]
                del starts[pos+1]
                if pos+1 in contributors:
                    contributors.remove(pos+1)
            if m == r - l + 1:
                contributors.add(l)
            if contributors:
                res = i+1
            starts[l] = r
            ends[r] = l
        return res if res is not None else -1

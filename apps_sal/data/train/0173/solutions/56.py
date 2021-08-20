class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        if n % 2:
            return False
        tbl = dict()
        for val in arr:
            r = val % k
            if tbl.get((k - r) % k, 0):
                tbl[(k - r) % k] -= 1
            else:
                tbl[r] = tbl.get(r, 0) + 1
        for (idx, cnt) in tbl.items():
            if cnt != 0:
                return False
        return True

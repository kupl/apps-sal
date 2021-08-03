from typing import Dict


class Solution:
    def _ds_find(ds: Dict[int, int], x: int) -> int:
        if ds.setdefault(x, x) != x:
            ds[x] = Solution._ds_find(ds, ds[x])

        return ds[x]

    def largestComponentSize(self, A: List[int]) -> int:
        ds = {}

        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    ds[Solution._ds_find(ds, i)] = Solution._ds_find(ds, x)
                    ds[Solution._ds_find(ds, i)] = Solution._ds_find(ds, x // i)

        return max(Counter(Solution._ds_find(ds, i) for i in A).values())

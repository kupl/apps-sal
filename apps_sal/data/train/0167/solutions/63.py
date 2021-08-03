class Solution:

    def eggDrop(self, floors, eggs, m):
        if floors <= 1:
            return floors
        if eggs == 1:
            return floors
        if (floors, eggs) in m:
            return m[(floors, eggs)]

        l, h = 0, floors

        while l < h:
            mid = (l + h) >> 1
            kelge, mele = self.eggDrop(mid - 1, eggs - 1, m), self.eggDrop(floors - mid, eggs, m)
            if kelge >= mele:
                h = mid
            else:
                l = mid + 1
        drops = 1 + max(self.eggDrop(l - 1, eggs - 1, m), self.eggDrop(floors - l, eggs, m))
        m[(floors, eggs)] = drops

        return drops

    def superEggDrop(self, K: int, N: int) -> int:

        return self.eggDrop(N, K, {})

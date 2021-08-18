class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int:

        dp = [[-1 for _ in range(floors + 1)] for _ in range(eggs + 1)]

        def search(eggs, floors):
            if eggs <= 0:
                return 0
            elif eggs == 1:
                return floors
            elif floors <= 1:
                return floors
            elif dp[eggs][floors] != -1:
                return dp[eggs][floors]

            l, r = 1, floors + 1
            while l < r:
                mid = l + (r - l) // 2
                broken = search(eggs - 1, mid - 1)
                intact = search(eggs, floors - mid)
                if broken < intact:
                    l = mid + 1
                else:
                    r = mid

            dp[eggs][floors] = 1 + search(eggs - 1, l - 1)
            return dp[eggs][floors]

        return search(eggs, floors)

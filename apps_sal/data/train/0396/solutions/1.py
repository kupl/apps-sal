class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # Say k = 3:
        # 1 mod 3 = 1
        # 10 mod 3 = 1
        # 100 mod 3 = 1
        # and we are done because each of the components contributes 1 to the modulo, and 3 of them completes it.

        # 1 mod 2 = 1
        # 10 mod 2 = 0
        # 100 mod 2 = 0
        # and all subsequent powers of 10 all contribute 0, so it's impossible.

        # Obviously all even K is impossible, because even * anything = even and 11...11 is always odd.

        # Is any odd K always possible? No. Clearly ***5 is not possible.
        # 1 mod 5 = 1
        # 10 mod 5 = 0
        # 100 mod 5 = 0
        # and so forth.

        # 1 mod 15 = 1
        # 10 mod 15 = 10
        # 100 mod 15 = 10
        # 1000 mod 15 = 10
        # and so forth.

        # Once a duplicate happens, why will it keep happening?
        # Say  1...1 (d digits) % K = m
        # Then 1....1 (d+1 digits) % K = (1...1 x 10 + 1) % K = (m x 10 + 1) % K
        # Thus the next mod is determined by the previous mod.
        if K % 10 not in [1, 3, 7, 9]:
            return -1
        m = 0
        for d in range(1, K + 1):
            m = (m * 10 + 1) % K
            if not m:
                return d
        return -1

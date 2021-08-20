import collections
import random
import heapq
import bisect
import math
import time


class Solution2:

    def solve(self, A1, A2):
        pass


class Solution:

    def gcd(self, a, b):
        if not b:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return b * a // self.gcd(b, a)

    def solve(self, n):
        out = 0
        MOD = 1000000007
        curr = {0: [1, 0]}
        for i in range(2 * n):
            new_curr = {}
            for (pos, (ways_clear, ways_taken)) in list(curr.items()):
                ways_clear = ways_clear % MOD
                ways_taken = ways_taken % MOD
                if pos:
                    if pos - 1 not in new_curr:
                        new_curr[pos - 1] = [0, 0]
                    new_curr[pos - 1][0] += ways_taken
                    new_curr[pos - 1][1] += ways_clear
                    out += ways_clear
                if pos < 2 * n - i:
                    if pos + 1 not in new_curr:
                        new_curr[pos + 1] = [0, 0]
                    new_curr[pos + 1][0] += ways_taken
                    new_curr[pos + 1][1] += ways_clear
                    out += ways_clear
            curr = new_curr
        return out % MOD


sol = Solution()
sol2 = Solution2()
for test_case in range(1):
    N = input()
    out = sol.solve(int(N))
    print(str(out))

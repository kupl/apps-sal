# 1545. Find Kth Bit in Nth Binary String: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
# Author: Ragy Morkos

#######################################################################

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0]
        for _ in range(2, n + 1):
            s = s + [1] + [1 - x for x in s][::-1]
        return str(s[k - 1])

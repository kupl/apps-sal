class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        (seen_odd, seen_even) = (set(), set())
        (odd_count, even_count) = (0, 1)
        psum = 0
        mod = 10 ** 9 + 7
        for a in arr:
            psum += a
            if psum % 2 == 0:
                ans = (ans + odd_count) % mod
                seen_even.add(psum)
                even_count += 1
            else:
                ans = (ans + even_count) % mod
                seen_odd.add(psum)
                odd_count += 1
        return ans

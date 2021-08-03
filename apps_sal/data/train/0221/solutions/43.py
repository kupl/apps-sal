class Solution:
    def longestDupSubstring(self, S: str) -> str:
        low = 0
        high = len(S) - 1
        result = ''
        nums = [ord(i) - ord('a') for i in S]
        mod = 2**63 - 1

        def rabin_karp(size):
            power = pow(26, size, mod)
            hash_val = 0
            hash_set = set()
            for i in range(size):
                hash_val = (hash_val * 26 + (nums[i])) % mod
            hash_set.add(hash_val)
            for i in range(size, len(S)):
                hash_val = (hash_val * 26 - (power * nums[i - size]) + nums[i]) % mod
                if hash_val in hash_set:
                    return i - size + 1
                else:
                    hash_set.add(hash_val)
            return -1
        while(low <= high):
            mid = low + (high - low) // 2
            pos = rabin_karp(mid)
            if pos == -1:
                high = mid - 1
            else:
                result = S[pos:pos + mid]
                low = mid + 1
        return result

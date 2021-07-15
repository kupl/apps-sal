class Solution:
    def search(self, S, mid) -> str:
        n = len(S)
        # convert string to array of integers to implement constant time slice
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        base = 26
        # mod value for the rolling hash function to avoid overflow
        MOD = 2**32
    
        # compute the hash of string S[:L]
        hash_ = 0
        for i in range(mid):
            hash_ = (hash_ * base + self.nums[i]) % MOD
              
        # already visited hashes of strings of length L
        visited = {hash_}
        # const value to be used often : a**L % mod
        aL = pow(base, mid, MOD)
        for start in range(1, n - mid + 1):
            # compute rolling hash in O(1) time
            hash_ = (hash_ * base - self.nums[start - 1] * aL + self.nums[start + mid - 1]) % MOD
            if hash_ in visited:
                return start
            visited.add(hash_)
        return -1
        
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers to implement constant time slice
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        base = 26
        # mod value for the rolling hash function to avoid overflow
        MOD = 2**32
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(S, mid) != -1:
                left = mid + 1
            else:
                right = mid - 1
               
        start = self.search(S, left - 1)
        return S[start: start + left - 1]
    
    
    
    


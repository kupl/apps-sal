class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        mod = 2 ** 31 - 1
        base = 26
        
        def get_ord(char: str):
            return ord(char) - ord('a')
        
        def find_duplicate(length) -> str:
            hashes = {}
            h = 1
            for i in range(length - 1):
                h = (h * base) % mod

            cur = 0
            for i in range(length):
                cur = (cur * base + get_ord(S[i])) % mod
            
            hashes[cur] = [0]

            for i in range(1, len(S) - length + 1):
                cur = ((cur - (get_ord(S[i-1]) * h)) * base + get_ord(S[i + length - 1])) % mod
                if cur in hashes:
                    for idx in hashes[cur]:
                        if S[idx: idx + length] == S[i: i + length]:
                            return S[i: i + length]
                    hashes[cur].append(i)
                else:
                    hashes[cur] = [i]
            return ''
        
        
        def helper(start, end):
            res = ''
            while start < end:
                length = (start + end) // 2 + 1
                r = find_duplicate(length)
                if len(r) > len(res):
                    res = r
                if not r:
                    end = length - 1
                else:
                    start = length
            return res

        return helper(0, len(S) - 1)

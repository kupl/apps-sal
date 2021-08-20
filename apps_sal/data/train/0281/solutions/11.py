class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        count = [0 for _ in range(26)]
        for (a, b) in zip(s, t):
            if a == b:
                continue
            shift = (ord(b) - ord(a)) % 26
            count[shift] += 1
        ch = ord('z') - ord('a')
        m = count[ch]
        for i in range(24, -1, -1):
            if count[i] > m:
                ch = i
                m = count[i]
        return (m - 1) * 26 + ch <= k

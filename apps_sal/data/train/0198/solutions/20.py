class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = head = subtotal = 0
        for tail in range(len(s)):
            subtotal += abs(ord(s[tail]) - ord(t[tail]))
            while subtotal > maxCost:
                subtotal -= abs(ord(s[head]) - ord(t[head]))
                head += 1
            max_len = max(max_len, tail - head + 1)
        return max_len

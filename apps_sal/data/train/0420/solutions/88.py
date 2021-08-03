class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        lu = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        def setFlags(flags: int, ch: str) -> int:
            if ch in lu.keys():
                mask = 1 << lu[ch]
                flags = flags ^ mask
            return flags
        FLAGS = 0
        seen = {0: -1}
        m = 0
        for i, c in enumerate(s):
            FLAGS = setFlags(FLAGS, c)
            if FLAGS in seen.keys():
                m = max(m, i - seen[FLAGS])
            else:
                seen[FLAGS] = i
        return m

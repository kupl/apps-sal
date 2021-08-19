class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        deltas = []
        if len(s) != len(t):
            return False
        for (i, c) in enumerate(s):
            t_index = ord(t[i]) - ord('a')
            s_index = ord(s[i]) - ord('a')
            deltas.append((t_index - s_index) % 26)
        m = collections.defaultdict(int)
        while k % 26 != 0:
            m[k % 26] += 1
            k -= 1
        for i in range(1, 26):
            m[i] += k // 26
        for d in sorted(deltas, reverse=True):
            if not d:
                continue
            if not m[d]:
                return False
            m[d] -= 1
        return True

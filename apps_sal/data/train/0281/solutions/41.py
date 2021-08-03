def dist(s_c, t_c):
    if s_c == t_c:
        return 0
    elif s_c < t_c:
        return ord(t_c) - ord(s_c)
    else:  # s_c > t_c
        return ord('z') - ord(s_c) + ord(t_c) - ord('a') + 1


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        distances = [0] * 26
        if len(s) != len(t):
            return False
        for s_c, t_c in zip(s, t):
            d = dist(s_c, t_c)
            if d != 0:
                distances[d] += 1
        for i, d in enumerate(distances):
            if d > 0:
                if (d - 1) * 26 + i > k:
                    return False
        return True

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 and s2 and s3:
            return True if s2 == s3 else False
        if not s2 and s1 and s3:
            return True if s1 == s3 else False
        if not s1 and not s2 and not s3:
            return True
        if (s1 and s2 and not s3) or (not s1 and not s2 and s3):
            return False

        result = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        result[0][0] = True
        for i in range(len(s1) + 1):
            il_idx = i - 1
            for j in range(len(s2) + 1):
                if i == j == 0:
                    continue
                if j > len(s3) - 1:
                    break
                s1_idx, s2_idx = i - 1, j - 1
                s1_char = s1[s1_idx] if s1_idx > -1 else None
                s2_char = s2[s2_idx] if s2_idx > -1 else None
                il_char = s3[il_idx + j]
                top = False if i == 0 else result[i - 1][j]
                left = False if j == 0 else result[i][j - 1]
                ds = set()
                if not left:
                    ds.add(s1_char)
                if not top:
                    ds.add(s2_char)
                result[i][j] = il_char in ds and (top or left)
                if (s1_char == s2_char == il_char) and top and left:
                    result[i][j] = True
        return result[-1][-1]

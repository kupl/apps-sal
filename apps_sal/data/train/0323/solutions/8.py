class Solution:
    def bruteForce(self, s1, s2, s3, i, j, k, string, m):
        try:
            return m[(i, j)]
        except KeyError:
            if k >= len(s3):
                if string == s3:
                    m[(i, j)] = True
                    return True
                else:
                    m[(i, j)] = False
                    return False
            else:
                x = False
                y = False
                xstring = string[:]
                if i < len(s1):
                    if(s1[i] == s3[k]):
                        if not string:
                            string = s1[i]
                        else:
                            string = string + s1[i]
                        x = self.bruteForce(s1, s2, s3, i + 1, j, k + 1, string, m)
                        if x == True:
                            m[(i, j)] = True
                            return True
                if j < len(s2):
                    if(s2[j] == s3[k]):
                        if not xstring:
                            xstring = s2[j]
                        else:
                            xstring = xstring + s2[j]
                        y = self.bruteForce(s1, s2, s3, i, j + 1, k + 1, xstring, m)
                m[(i, j)] = x or y
                return x or y

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2 and not s3:
            return True
        if not s1:
            if s2 == s3:
                return True
            else:
                return False
        if not s2:
            if s1 == s3:
                return True
            else:
                return False
        if len(s3) != len(s1) + len(s2):
            return False
        return self.bruteForce(s1, s2, s3, 0, 0, 0, "", {})

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = -1
        right = 0
        result = ""

        totalMatch = 0
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1

        for right in range(len(s)):
            c = s[right]
            if c in d:
                d[c] -= 1
                if d[c] >= 0:
                    totalMatch += 1

                    if left == -1:
                        left = right

                    if totalMatch == len(t):
                        if result == "" or len(result) > right - left:
                            result = s[left: right + 1]

                        d[s[left]] += 1
                        totalMatch -= 1
                        while left < right:
                            left += 1

                            if s[left] in d:
                                if d[s[left]] < 0:
                                    d[s[left]] += 1
                                else:
                                    break

                elif c == s[left]:
                    d[c] += 1
                    while left < right:
                        left += 1
                        if s[left] in d:
                            if d[s[left]] < 0:
                                d[s[left]] += 1
                            else:
                                break
        return result

class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.maps = dict()
        return self.dfs(s, p)

    def dfs(self, s, p):
        key = (s, p)
        if key in self.maps:
            return self.maps[key]
        if not s and (not p):
            return True
        if s and (not p):
            return False
        if len(p) > 1 and p[1] == '*':
            if s and s[0] == p[0] or (p[0] == '.' and s):
                self.maps[key] = self.dfs(s[1:], p[2:]) or self.dfs(s[1:], p) or self.dfs(s, p[2:])
            else:
                self.maps[key] = self.dfs(s, p[2:])
        elif s and s[0] == p[0] or (p[0] == '.' and s):
            self.maps[key] = self.dfs(s[1:], p[1:])
        return self.maps[key] if key in self.maps else False

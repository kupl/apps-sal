class Solution:

    def helper(self, level, chars):
        if level == len(chars):
            temp1 = ''.join(chars)
            if temp1[0] == '0':
                return 0
            if temp1 in self.been:
                return self.been[temp1]
            temp = int(temp1)
            while temp != 1:
                if temp % 2 == 0:
                    temp = int(temp / 2)
                else:
                    self.been[temp1] = 0
                    return 0
            self.been[temp1] = 1
            return 1
        seen = set()
        for i in range(level, len(chars)):
            if chars[i] in seen:
                continue
            (chars[level], chars[i]) = (chars[i], chars[level])
            h = self.helper(level + 1, chars)
            if h == 1:
                return 1
            (chars[level], chars[i]) = (chars[i], chars[level])
            seen.add(chars[i])
        return 0

    def reorderedPowerOf2(self, N: int) -> bool:
        N = str(N)
        chars = [char for char in N]
        seen = set()
        self.been = {}
        for i in range(0, len(chars)):
            if self.helper(i, chars):
                return True
        return False

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = [c for c in s]
        if k == 1:
            temp = []
            for i in range(len(s)):
                temp_s = s[i:] + s[:i]
                temp.append(''.join(temp_s))
            temp.sort()
            return temp[0]
        else:
            return ''.join(sorted(s))

class Solution:

    def maxDiff(self, num: int) -> int:
        a = []
        s = str(num)
        for i in range(0, 10):
            for j in s:
                n = s.replace(j, str(i))
                m = int(n)
                if m != 0 and n[0] != '0':
                    a.append(m)
        diff = max(a) - min(a)
        return diff

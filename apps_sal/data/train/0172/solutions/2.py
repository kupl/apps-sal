class Solution:
    def maxDiff(self, num: int) -> int:
        replaces = []
        num = str(num)
        for i in range(0, 10):
            for j in range(0, 10):
                rep_num = num.replace(str(i), str(j))
                if rep_num[0] != '0':
                    replaces.append(int(rep_num))
        return max(replaces) - min(replaces)

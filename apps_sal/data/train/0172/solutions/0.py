class Solution:

    def maxDiff(self, num: int) -> int:
        if num < 10:
            return 8
        a = b = str(num)
        i = 0
        while i < len(a):
            if a[i] == '9':
                i += 1
            else:
                a = a.replace(a[i], '9')
                break
        if b[0] != '1':
            b = b.replace(b[0], '1')
        else:
            i = 1
            while i < len(b):
                if b[i] == '1' or b[i] == '0':
                    i += 1
                else:
                    b = b.replace(b[i], '0')
                    break
        return int(a) - int(b)

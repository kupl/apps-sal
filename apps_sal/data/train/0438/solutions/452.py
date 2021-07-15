class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        s = '1' * n
        sm = '1' * m
        if m == n:
            return n
        for ind, i in enumerate(arr[::-1]):
            #print(s, i, sm)
            s = s[:i-1] +  '0' + s[i:]
   # print((i - 1 + m < n ))
   #          print(s[i : i  + m] , sm)
   #          print(i, m, n)
            if (i - 1 - m >= 0 and s[i - 1 - m: i - 1] == sm and ((i - 1 - m == 0) or s[i - 2 - m] == '0')) or  (i  + m <= n and s[i : i  + m] == sm and ((i + m == n ) or s[i + m ] == '0')):
                return n - ind - 1
        return -1


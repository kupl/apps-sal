class Solution:

    def minSteps(self, n):
        m = n
        sum = 0
        tmp = 2
        if m == 1:
            return 0
        if m == 2:
            return 2
        else:
            while m > tmp:
                k = m % tmp
                if k == 0:
                    m = m / tmp
                    sum += tmp
                else:
                    tmp = tmp + 1
            sum = sum + tmp
            return sum
        '\n         :type n: int\n         :rtype: int\n         '

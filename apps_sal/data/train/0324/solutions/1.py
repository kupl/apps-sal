class Solution:

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        sn = str(n)
        nlen = len(sn)
        if nlen == 1:
            return -1
        else:
            (i, j) = (-1, -2)
            (end, check) = (i, True)
            sl = list(sn)
            while j != -nlen and sl[j] >= sl[i]:
                if sl[end] < sl[j] and check:
                    end = j
                    check = False
                i -= 1
                j -= 1
            if sl[j] == sl[end]:
                if i > j:
                    end = i
            if sl[j] == min(sl):
                end = -1
            (sl[j], sl[end]) = (sl[end], sl[j])
            (front, back) = (sl[:j + 1], sorted(sl[j + 1:]))
            result = int(''.join(front + back))
            return result if result > n and result < 2147483647 else -1

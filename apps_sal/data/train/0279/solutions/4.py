class Solution:
    def getPermutation(self, n, k):
        """
        Input:
            n:  int
            k:  int
        Output:
            str
        """
        return self.__getPerm(set(range(1, n + 1)), k)

    def __getPerm(self, set_n, k):
        """
        Input:
            set_n:  set:    set of available number
            k:  int:        k-th permuation
        Output:
            str
        """
        if not set_n:
            return ''

        arr_n = sorted(set_n)
        n = len(arr_n)
        i = 0
        fac = 1     # i!

        while i + 1 < n:
            i += 1
            fac *= i

        # fac = (n-1)!
        i_digit = (k - 1) // fac
        k = k - i_digit * fac
        digit = arr_n[i_digit]

        set_n.remove(digit)
        return str(digit) + self.__getPerm(set_n, k)

class Solution:
    def countLeadingOne(self, w):
        if w[0] == '0':
            return 1
        elif w[0:3] == "110":
            return 2
        elif w[0:4] == '1110':
            return 3
        elif w[0:5] == '11110':
            return 4
        else:
            return -1

    def checkStartWith10(self, L, l):
        #print(L, l)
        if len(L) != l:
            return False

        for w in L:
            if w.startswith('10') == False:
                return False

        return True

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        A = []
        for d in data:
            A.append(format(d, '08b'))

        i = 0

        while i < len(A):
            l = self.countLeadingOne(A[i])
            if l == -1:
                return False

            if l > 1:
                if self.checkStartWith10(A[i + 1:i + l], l - 1) == False:
                    return False

            i += l

        return True

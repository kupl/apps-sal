class Solution:

    hashMap = {}
    outPut = []

    def helper(self, n, string, length, opened, openUsed):

        if length == n * 2:
            if string not in self.outPut:
                self.outPut.append(string)
            return

        if string in self.hashMap:
            return
        else:
            self.hashMap[string] = 1

        if opened == 0:
            tempOpened = 1
            tempOpenUsed = openUsed + 1
            self.helper(n, string + '(', length + 1, tempOpened, tempOpenUsed)

        if opened > 0:
            tempOpened = opened - 1
            self.helper(n, string + ')', length + 1, tempOpened, openUsed)

        if openUsed < n:
            tempOpened = opened + 1
            tempOpenUsed = openUsed + 1
            self.helper(n, string + '(', length + 1, tempOpened, tempOpenUsed)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.hashMap = {}
        self.outPut = []
        self.helper(n, "", 0, 0, 0)

        return self.outPut

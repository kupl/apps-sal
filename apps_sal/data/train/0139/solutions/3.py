import copy


class Solution:

    def checkLexOrder(self, A: List[str]):
        if A == sorted(A):
            return True
        else:
            return False

    def findDelIndices(self, A: List[str]):
        iter_ = len(A[0])
        to_be_del = []
        temp = [''] * len(A)
        for i in range(iter_):
            if self.checkLexOrder([x[i] for x in A]) == True:
                temp = [temp[j] + A[j][i] for j in range(len(A))]
            else:
                temp_ = [temp[j] + A[j][i] for j in range(len(A))]
                if self.checkLexOrder(temp_) == True:
                    temp = [temp[j] + A[j][i] for j in range(len(A))]
                else:
                    to_be_del.append(i)
        return len(to_be_del)

    def minDeletionSize(self, A: List[str]) -> int:
        if self.checkLexOrder(A):
            return 0
        else:
            return self.findDelIndices(A)

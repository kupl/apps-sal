class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        groupCount = dict()
        n = len(arr)
        parents = [0] * n

        lastM = -1
        mCnt = 0
        for i, p in enumerate(arr):
            leftParent = self.getParent(p - 1, parents)
            rightParent = self.getParent(p + 1, parents)
            parents[p - 1] = p    # its own parent
            if leftParent == 0 and rightParent == 0:
                groupCount[p] = 1
                newCnt = 1
            elif leftParent != 0 and rightParent != 0:
                newCnt = groupCount[leftParent] + groupCount[rightParent] + 1
                self.mergeGroups(leftParent, p, parents)
                self.mergeGroups(rightParent, p, parents)
            elif leftParent != 0:
                newCnt = groupCount[leftParent] + 1
                self.mergeGroups(leftParent, p, parents)
            else:
                newCnt = groupCount[rightParent] + 1
                self.mergeGroups(rightParent, p, parents)

            if leftParent != 0 and groupCount[leftParent] == m:
                mCnt -= 1

            if rightParent != 0 and groupCount[rightParent] == m:
                mCnt -= 1

            groupCount[p] = newCnt

            if newCnt == m:
                mCnt += 1

            if mCnt > 0:
                lastM = i + 1

        return lastM

    def getParent(self, p: int, parents: List[int]) -> int:
        if p <= 0 or p > len(parents):
            return 0

        if p == parents[p - 1]:
            return p

        return self.getParent(parents[p - 1], parents)

    def mergeGroups(self, pp, p, parents):
        parents[pp - 1] = p

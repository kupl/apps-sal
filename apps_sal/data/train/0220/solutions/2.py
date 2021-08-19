class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        wn = min(len(customers), X)
        print(('wn', wn))
        wList = [0] * len(customers)
        for i in range(len(customers)):
            if grumpy[i]:
                wList[i] = customers[i]
            else:
                wList[i] = 0
        print(('list', wList))
        mwsum = sum(wList[0:wn])
        nws = mwsum
        print(mwsum)
        for j in range(wn, len(wList)):
            nws = nws - wList[j - wn] + wList[j] if wn > 1 else wList[j]
            mwsum = max(mwsum, nws)
            print(nws)
        for i in range(len(customers)):
            if grumpy[i] == 0:
                mwsum += customers[i]
        return mwsum

class Solution:
    def knightDialer(self, n: int) -> int:
        movesMap=dict()
        MOD=10**9+7
        movesMap[0]=[4,6]
        movesMap[1]=[6,8]
        movesMap[2]=[7,9]
        movesMap[3]=[4,8]
        movesMap[4]=[0,3,9]
        movesMap[5]=[]
        movesMap[6]=[0,1,7]
        movesMap[7]=[2,6]
        movesMap[8]=[1,3]
        movesMap[9]=[2,4]
        totalCount=0
        for i in range(10):
            curPos=[0]*10
            curPos[i]=1
            for count in range(n-1):
                nextPos=[0]*10
                for curIndex in range(10):
                    if curPos[curIndex]>0:
                        for nextIndex in movesMap[curIndex]: 
                            nextPos[nextIndex]+=curPos[curIndex]
                            nextPos[nextIndex]%=MOD
                curPos=nextPos
            for finIndex in range(10):
                totalCount+=curPos[finIndex]
                totalCount%=MOD
        return totalCount

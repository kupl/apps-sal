class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        '''
        [5,0,3,8,6]
         mn=[5,0,0,0]
         mx=[5,5,5,8,8]

        [1,1,1,0,6,12]
        mx=[1,1,1,1,6,12]
        '''
        ml = 0
        mx = -1e9
        mxsofar = 1e9
        for i, a in enumerate(A):
            mx = max(a, mx)
            if a < mxsofar:
                ml = i + 1
                mxsofar = mx
                # print(\"a=%d,mx=%d,mxsofar %d\"%(a,mx,mxsofar))

        return ml

class Solution:
    def maxDotProduct(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        
        mem = [[None]*n for i in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mem[i][j] = nums1[i] * nums2[j]
        #myPrint(mem)

        for i in range(m-1,-1,-1):
            #max_ = mem[i+1][n-1] if i<m-1 else -1001
            for j in range(n-1,-1,-1):
                #print('i,j : ' ,i,j)
                #if mem[i][j] < 0 and max_ < 0: 
                #    mem[i][j] = max(mem[i][j], max_)
                #else:
                #print('here2 :', max_)
                #mem[i][j] = max(mem[i][j] + max_, max(mem[i][j], max_))
                max_ = mem[i+1][j+1] if i+1<m and j+1<n else -1001
                mem[i][j] = max(mem[i][j] + max_, max(mem[i][j], max_))
                #print('here : ', mem[i][j])
                mem[i][j] = max(mem[i][j], 
                                mem[i][j+1] if j<n-1 else -1001)
                mem[i][j] = max(mem[i][j], 
                                mem[i+1][j] if i<m-1 else -1001)
                #max_ = max(max_, mem[i+1][j] if i<m-1 else -1001)
                #myPrint(mem)
        return mem[0][0]

class Solution:
    def binary_search(self,A,k,n):
        lo = 0
        hi = n
        mid = (lo+hi)//2
        while lo<hi:
            if A[k-1][mid-1]==A[k][n-mid]:
                return mid
            if A[k-1][mid-1]>A[k][n-mid]:
                hi = mid
            else:
                lo = mid+1
            mid = (lo+hi)//2
            
        return lo
    def superEggDrop(self, K: int, N: int) -> int:
        if N==1:
            return 1
        # k=0
        # n=N
        # while n>0:
        #     k+=1
        #     n//=2
        # if K>k:
        #     return k
        A = [[0 for n in range(N+1)] for k in range(K+1)]
        
        for n in range(N+1):
            A[1][n] = n
        for k in range(K+1):
            A[k][1] = 1
            A[k][2] = 2
        
        for k in range(2,K+1):
            low=1
            for n in range(3,N+1):
                # linear search
                # m=1
                # while A[k-1][m-1]<A[k][n-m]:
                #     m+=1
                
                #binary search
                # m = self.binary_search(A,k,n)
                # A[k][n] = 1+max(A[k-1][m-1],A[k][n-m])
                
                # tip-toe
                # print('k =',k,' n = ',n,low,'    ', A[k-1][low],'   ',A[k][n-low-1],'   ',A[k][n])
                if A[k-1][low]<A[k][n-low-1]:
                    low+=1
                  
                A[k][n] = 1+A[k-1][low]
                # print('k =',k,' n = ',n,low,'    ', A[k-1][low],'   ',A[k][n-low-1],'   ',A[k][n])
                # print('')
        return A[-1][-1]

class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        ''' returns True if indices i and j can be found such that A[0]+...+A[i]==A[i+1]+...+A[j]==A[j+1]+...+A[-1]

        Algo: form [A[0], A[0]+A[1], A[0]+A[1]+A[2], ..., sum(A)]
        if A can be partitioned, then n=sum(A) is a multiple of 3,
        2*n//3 must appear at some index j, and n//3 must appear at some index i<j'''
        if len(A)<3:
            return False
        for i in range(1,len(A)):
            A[i] = A[i-1]+A[i]
        end_value=A[-1]
        if end_value%3!=0:
            return False
        index=len(A)-2
        while A[index] != 2*end_value//3:
            index-=1
            if index==0:
                return False
        index-=1
        while A[index] != end_value//3:
            index-=1
            if index<0:
                return False
        return True

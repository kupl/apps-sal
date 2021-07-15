class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        return self.subarraysWithKMax(A,K) - self.subarraysWithKMax(A,K-1)
    
    def subarraysWithKMax(self, A, K):
        k = 0
        count = dict()
        i, start = 0, 0
        res = 0
        while i < len(A):
            if A[i] not in count:
                k+=1
                count[A[i]] = 1
            else:
                count[A[i]] += 1
            i+=1
            
            while start<i and k>K:
                count[A[start]] -= 1
                if count[A[start]] == 0:
                    del count[A[start]]
                    k -= 1
                start += 1
            res += i-start
        return res

